from django.contrib.auth import get_user_model
from rest_framework import status, generics
from rest_framework.views import APIView
from photolair.models import Image
from rest_framework.permissions import (
  AllowAny,
  IsAuthenticated,
)
from rest_framework.permissions import SAFE_METHODS
from .permissions import IsUserOwnerOnly
from .serializers import (
  RegisterUserSerializer,
  UserSerializer,
  ImageSerializer
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
    permission_classes = [IsUserOwnerOnly,]


class ImageListView(generics.ListCreateAPIView):
    """
    Image List Endpoint
    - GET: Retrieve a list of images
    - POST: Uploads an image plus its accompanying information
    """

    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    
    def get_permissions(self):
        """
        Anyone can view an image, however, to upload a new image the 
        user must be authenticated.
        """
        if self.request.method == SAFE_METHODS:
            self.permission_classes = [AllowAny,]
        else:
            self.permission_classes = [IsAuthenticated,]
        return super(ImageListView, self).get_permissions()


class ImageDetailView(APIView):
    """
    Image Detail Endpoint
    - GET: Download image for request user and transfer funds
    - PUT/PATCH: Update image details for image owned by request user
    - DELETE: Delete the image owned by request user
    """
    pass