import uuid
import core.settings as app_settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from ..managers import CustomUserManager


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
        help_text=_('Account balance of credits available to the user'),
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
        