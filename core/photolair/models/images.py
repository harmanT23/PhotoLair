import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from profanity.validators import validate_is_profane

from .users import User
from ..utilities import upload_image_path


class Image(models.Model):
    """
    Defines model for the images a user uploads.
    """
    id = models.UUIDField(
      _('ID'),
      primary_key=True, 
      default=uuid.uuid4, 
      editable=False,
      help_text=_('Image ID is a uuid.'),
    )

    user = models.ForeignKey(
        User,
        verbose_name=_('User'),
        on_delete=models.CASCADE, 
        help_text=_('Image belongs to associated User.'), 
    )
    
    image_name = models.CharField(
        _('Image Name'),
        max_length=100,
        validators=[validate_is_profane],
        blank=False,
        help_text=_('Name of image specified by user.'),
    )

    image = models.ImageField(
        _('Image'),
        blank=False,
        upload_to=upload_image_path, 
        help_text=_('URL to image file'),
    )

    inventory = models.PositiveBigIntegerField(
        _('inventory'),
        blank=False,
        default=0,
        help_text=_('Defines number of available image downloads.'),
    )

    price = models.PositiveBigIntegerField(
        _('Price'),
        blank=False,
        default=0,
        help_text=_('Defines price (in credits) for each image download.'),
    )

    created_at = models.DateTimeField(
        _('Created At'),
        auto_now=True, 
        editable=False,
        help_text=_('Indicates when image instance was created.'),
    )

    updated_at = models.DateTimeField(
        _('Updated At'),
        auto_now=True,
        editable=True,
        help_text=_('Indicates when image instance was last updated.'),
    )

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')

    def __str__(self):
        return self.image_name
        