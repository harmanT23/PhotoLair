from django.contrib import admin
from .models import Image
from django.contrib.auth import get_user_model

User = get_user_model()


# Register your models here.
admin.site.register(User)
admin.site.register(Image)
