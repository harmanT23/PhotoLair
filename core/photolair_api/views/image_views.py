import os
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
    - GET: Retrieve all images in the dataset
    - POST: Upload an image and its accompanying information
    """

    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    
    def get_permissions(self):
        """
        Retrieving a list of all images in the database requires 
        no authentication, however, to upload a new image the 
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
    - GET: Get image specified by id as a blob for authenticated user, 
      check if user can afford image and in stock, and perform transaction.
    - PATCH: Update image details for image specified by id
    - DELETE: Delete the image specified by id

    Note: Updating and deleting an image can only be done by the original
    author of the image.
    """

    def get_permissions(self):
        """
        Any user can request to download an image but only users that own 
        the associated image can edit/delete it.
        """
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAuthenticatedAndImageOwner] 
        return super(ImageDetailView, self).get_permissions()
    
    def _download_image_send_blob(self, image):
        """
        Behaviour is dependent on whether backend is using S3. 

        With S3: Downloads an image from S3 url, save it to a temp file 
        and send the image as a blob in the http response.

        Without S3: simply read file from local storage, encode it to base 64
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
            file_path = os.path.join(app_settings.MEDIA_ROOT, image.image.name)
            image_file = open(file_path, 'rb')
            return FileResponse(image_file, as_attachment=True)
            

    def get(self, request, image_id, format=None):
        """
        Get the image specified by image_id for the authenticated user,
        perform validation checks and then transaction. The image itself is
        returned as a blob. 
        """
        image = buy_image(request.user, image_id)
        return self._download_image_send_blob(image)

    def patch(self, request, image_id, format=None):
        """
        Update details of image specified by id such as it title, price 
        and inventory
        """
        image = get_object_or_404(Image, pk=image_id)

        serializer = ImageUpdateSerialier(image, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, image_id, format=None):
        """
        Delete image specified by id
        """
        image = get_object_or_404(Image, pk=image_id)
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
