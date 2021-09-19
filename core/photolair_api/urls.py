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
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/blacklist/', BlackListTokenView.as_view(), name='blacklist_token'),
    path('users/', UserCreateView.as_view()),
    path('users/me/', MeView.as_view()),
    path('users/<uuid:user_id>', UserDetailView.as_view()),
    path('images/', ImageListView.as_view()),
    path('images/<uuid:image_id>', ImageDetailView.as_view()),
]
