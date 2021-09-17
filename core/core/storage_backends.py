from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class PublicMediaStorage(S3Boto3Storage):
    """
    Defines settings for storage of public media on S3
    """
    location = 'media'
    default_acl = 'public-read'
    file_overwrite = False
    