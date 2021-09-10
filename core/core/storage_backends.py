from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    """
    Defines settings for storage of static files on S3
    """
    location = 'static'
    default_acl = 'public-read'


class PublicMediaStorage(S3Boto3Storage):
    """
    Defines settings for storage of media on S3
    """
    location = 'media'
    default_acl = 'public-read'
    file_overwrite = False