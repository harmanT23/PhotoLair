from django.urls import path
from rest_framework.schemas import get_schema_view
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
    path('', get_schema_view(
        title="PhotoLair API",
        description="API for creating a image marketplace",
        version="1.0.0"
    ), name='openapi-schema'),
]
