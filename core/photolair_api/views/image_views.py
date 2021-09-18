import os
import base64
import requests
import core.settings as app_settings
from tempfile import NamedTemporaryFile
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)
from ..permissions import IsAuthenticatedAndImageOwner
from ..serializers import (
    ImageSerializer,
    ImageUpdateSerialier,
)
from ..services import buy_image
from photolair.models import Image


class ImageListView(generics.ListCreateAPIView):
    """
    Image List Endpoint
    - GET: Retrieve a list of images
    - POST: Uploads an image and its accompanying information
    """

    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    
    def get_permissions(self):
        """
        Anyone can view an image, however, to upload a new image the 
        user must be authenticated.
        """
        if self.request.method == 'GET':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]
        
        return super(ImageListView, self).get_permissions()


class ImageDetailView(APIView):
    """
    Image Detail Endpoint
    - GET: Download image by id for request user and transfer funds
    - PATCH: Update image details for image owned by request user
    - DELETE: Delete the image owned by request user
    """

    def get_permissions(self):
        """
        For the endpoints exposted by this view, any user can download an image
        but only users that own the associated image can edit/delete it
        """
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAuthenticatedAndImageOwner] 
        return super(ImageDetailView, self).get_permissions()
    
    def _download_image_send_blob(self, image):
        """
        Behaviour is dependent on whether backend is using S3. 

        If using S3, downloads an image from given url, save it to a temp file 
        and finally send the image as a blob in the http response.

        Else, simply read file from local storage, encode it to base 64
        and return the image as a blob in the http response. 
        """
        
        if app_settings.AWS_S3:
            tempFile = NamedTemporaryFile(mode='w+b', suffix='jpeg')
            res = requests.get(image.image.url, stream=True)

            if not res.ok:
                return Response(status=res.status_code)
            
            for block in res.iter_content(chunk_size=1024):
                if not block:
                    break
                tempFile.write(block)
            tempFile.seek(0,0)
            return FileResponse(tempFile, as_attachment=True)

        else:
            file_path = (
                app_settings.MEDIA_ROOT + image.image.url.split('/mediafiles')[-1]
            )
            image_file = open(file_path, 'rb')
            return FileResponse(image_file, as_attachment=True)
            

    def get(self, request, image_id, format=None):
        """
        Get the image specified by image_id for the request user,
        perform validation checks and transaction. The image itself is
        returned as a blob. 
        """
        image = buy_image(request.user, image_id)

        return self._download_image_send_blob(image)

    def patch(self, request, image_id, format=None):
        """
        Update details of an image such as title, price and inventory
        """
        image = get_object_or_404(Image, pk=image_id)

        serializer = ImageUpdateSerialier(image, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, image_id, format=None):
        """
        Delete image specified by user
        """
        image = get_object_or_404(Image, pk=image_id)
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
