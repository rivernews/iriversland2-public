from django.conf import settings

# `S3Boto3Storage` implementation source code: https://github.com/jschneier/django-storages/blob/master/storages/backends/s3boto3.py
from storages.backends.s3boto3 import S3Boto3Storage


class MediaStorage(S3Boto3Storage):
    bucket_name = settings.MEDIA_FILES_BUCKET_NAME

    # Have to manually set custom domain to honor bucket name, otherwise by default it will always use settings.AWS_S3_CUSTOM_DOMAIN as domain name to contruct any file url
    # see implementation: https://github.com/jschneier/django-storages/blob/master/storages/backends/s3boto3.py
    custom_domain = '{}.s3.amazonaws.com'.format(bucket_name)

class StaticStorage(S3Boto3Storage):
    bucket_name = settings.STATIC_FILES_BUCKET_NAME