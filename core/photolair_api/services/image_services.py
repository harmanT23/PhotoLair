from django.db.models import F
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.exceptions import APIException
from django.contrib.auth import get_user_model

from photolair.models import Image

User = get_user_model()

def _remove_sold_out_image(image):
  """
  Deletes an image that is sold out
  """
  image.delete()

def buy_image(buy_user, image_id):
    """
    Performs action of purchasing image specified by image_id for 
    user defined by buy_user_id. Validation checks are done to ensure
    user has enough funds and that the image is still in stock.
    """

    image = get_object_or_404(Image, pk=image_id)
            
    if image.inventory == 0:
        _remove_sold_out_image(image)
        raise APIException(
            'Image is sold out.', 
            code=status.HTTP_403_FORBIDDEN
        )
        
    if buy_user.credits < image.price:
        raise APIException(
            'User does not have enough credits.', 
            code=status.HTTP_402_PAYMENT_REQUIRED
        )

    sell_user = User.objects.get(pk=image.user.id)

    # Only expense and reduce stock if buy and sell user are different
    if sell_user.id != buy_user.id:
        # Use F expression to avoid race conditions and work on DB data direct
        buy_user.credits = F('credits') - image.price
        buy_user.save()

        sell_user.credits = F('credits') + image.price
        sell_user.save()

        image.inventory = F('inventory') - 1
        image.save()

    return image
