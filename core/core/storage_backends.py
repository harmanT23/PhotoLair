from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class PublicMediaStorage(S3Boto3Storage):
    """
    Settings for storage of media on public s3 bucket
    """
    location = 'media'
    default_acl = 'public-read'
    file_overwrite = False
    