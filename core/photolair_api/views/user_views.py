from rest_framework import generics
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.permissions import AllowAny

from ..permissions import IsAuthenticatedAndOwner
from ..serializers import (
    RegisterUserSerializer,
    UserSerializer,
)

User = get_user_model()


class UserCreateView(generics.CreateAPIView):
    """
    User Create Endpoint
    - POST: Registers a new user given username and password
    """
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
    permission_classes = [AllowAny,]


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    User Detail Endpoint
    - GET: Get a user by id
    - PUT/PATCH: Update a user by id
    - DELETE: Delete a user by id
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedAndOwner,]

    def get_object(self, queryset=None, **kwargs):
        """
        Get the user instace for specified by the authenticated user.
        If authenticated user does not math requested user raises HTTP
        error.
        """
        user_id = self.kwargs.get('user_id')
        if self.request.user.id != user_id:
            raise APIException(
                'Authenticated user cannot view or edit other users profiles',
                code=status.HTTP_401_UNAUTHORIZED
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
