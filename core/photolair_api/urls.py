from django.urls import path
from .views import (
  UserCreateView,
  UserDetailView,
  ImageListView,
  ImageDetailView
)

app_name = 'photolair_api'

urlpatterns = [
    path('users/', UserCreateView.as_view()),
    path('users/<uuid:user_id>', UserDetailView.as_view()),
    path('images/', ImageListView.as_view()),
    path('images/<uuid:image_id>', ImageDetailView.as_view()),
]
