import uuid
import core.settings as app_settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from .image_handler import upload_image_path
from profanity.validators import validate_is_profane


class User(AbstractUser):
    """
    User model that extends Django's built-in AbstractUser model.
    """
    id = models.UUIDField(
        _('ID'),
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False,
        help_text=_('User ID is a uuid.'),
    )

    credits = models.PositiveBigIntegerField(
        _('Credits'),
        blank=True,
        default=app_settings.DEFAULT_CREDITS,
        help_text=_('Default number of credits each user starts with'),
    )

    created_at = models.DateTimeField(
        _('Created At'),
        auto_now=True, 
        editable=False,
        help_text=_('Indicates when user instance was created.'),
    )

    updated_at = models.DateTimeField(
        _('Updated At'),
        auto_now=True,
        editable=True,
        help_text=_('Indicates when user instance was last updated.'),
    )

    objects = CustomUserManager()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.username


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
        help_text=_('Name of image.'),
    )

    image = models.ImageField(
        _('Image'),
        blank=False,
        upload_to=upload_image_path, 
        help_text=_('URL to image file/'),
    )

    inventory = models.PositiveBigIntegerField(
        _('Credits'),
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
