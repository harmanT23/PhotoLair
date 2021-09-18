from django.dispatch import receiver
from django.db.models.signals import post_delete

from ..models import Image

@receiver(post_delete, sender=Image)
def Image_postdelete(sender, instance, *args, **kwargs):
    """
    Post delete signal to handle deleting an image that is out of stock
    """ 
    try:
        instance.image.delete(save=False)
    except Exception as e:
        raise Exception('Unable to delete image.', e)
