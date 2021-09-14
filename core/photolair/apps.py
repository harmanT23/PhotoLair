from django.apps import AppConfig


class PhotolairConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'photolair'

    def ready(self):
        """
        Register signals for application
        """
        from . import signals
