from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.exceptions import APIException
from photolair.models import Image
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import (
  AllowAny,
  IsAuthenticated,
)
from .permissions import (
    IsAuthenticatedAndOwner, 
    IsAuthenticatedAndImageOwner,
)
from .serializers import (
  RegisterUserSerializer,
  UserSerializer,
  ImageSerializer,
  ImageUpdateSerialier,
)
from .services import (
    buy_image,
)

User = get_user_model()


class UserCreateView(generics.CreateAPIView):
    """
    User Create Endpoint
    - POST: Registers a new user
    """
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
    permission_classes = [AllowAny,]


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    User Detail Endpoint
    - GET: Get a user by id
    - PUT/PATCH: Update a user by id
    - DELETE: Delete a user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedAndOwner,]

    def get_object(self, queryset=None, **kwargs):
        """
        Get the user object for the request user.
        If request user does not match url. Raise exception.
        """
        user_id = self.kwargs.get('user_id')
        if self.request.user.id != user_id:
            raise APIException(
                'Authenticated user cannot view or edit other users profiles'
            )
        return get_object_or_404(User, id=user_id)


class MeView(generics.RetrieveUpdateDestroyAPIView):
    """
    Me View Endpoint
    - GET: Get the authenticated user's profile details
    - PATCH: Update the authenticated user's profile
    - DELETE: Delete the authenticated user's profie
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedAndOwner,]

    def get_object(self, queryset=None, **kwargs):
        """
        Get the user object of the authenticated user
        """
        return self.request.user


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
    serializer_class = ImageSerializer

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
    
    def get(self, request, image_id, format=None):
        """
        Get the image specified by image_id for the request user,
        perform validation checks and transaction.
        """
        image_url = buy_image(request.user, image_id)
        return Response(image_url)

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

class BlackListTokenView(APIView):
    """
    Used to blacklist refresh tokens after a user logs out.
    """
    permission_classes = [AllowAny,]

    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
