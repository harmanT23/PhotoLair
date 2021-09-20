from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from .views import (
    UserCreateView,
    UserDetailView,
    MeView,
    ImageListView,
    ImageDetailView,
    BlackListTokenView,
)

app_name = 'photolair_api'

urlpatterns = [
    # Authentication Endpoints
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/blacklist/', BlackListTokenView.as_view(), name='blacklist_token'),
    # User Endpoints
    path('users/', UserCreateView.as_view(), name='user_create'),
    path('users/me/', MeView.as_view(), name='me'),
    path('users/<uuid:user_id>', UserDetailView.as_view(), name='user_detail'),
    # Image Endpoints
    path('images/', ImageListView.as_view(), name='image_list'),
    path('images/<uuid:image_id>', ImageDetailView.as_view(), name='image_detail'),
]
