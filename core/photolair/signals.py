import os
from django.db.models.signals import post_delete
from django.core.files.storage import get_storage_class
from django.dispatch import receiver
from .models import Image

django_storage = get_storage_class()


@receiver(post_delete, sender=Image)
def Image_postdelete(sender, instance, *args, **kwargs):
    """
    Post delete signal to handle deleting an image that is out of stock
    """
    try:
        instance.delete_image()
    except Exception as e: #TODO: Don't send this to front end
        raise Exception('Unable to delete image.', e)
