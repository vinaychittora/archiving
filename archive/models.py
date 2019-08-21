from django.db import models
from django_mysql.models import JSONField


class Archive(models.Model):
    PROCESSING = 'P'
    FAILED = 'F'
    COMPLETE = 'C'
    REQUEST_STATUS = [
        (PROCESSING, 'Processing'),
        (FAILED, 'Failed'),
        (COMPLETE, 'Completed')
    ]

    bulk_hash = models.CharField(unique=True, max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    request_status = models.CharField(
        max_length=2,
        choices=REQUEST_STATUS,
        default=PROCESSING
    )


class FileEntitiy(models.Model):
    FOUND = 'F'
    NOT_FOUND = 'N'
    FILE_STATUS = [
        (FOUND, 'Found'),
        (NOT_FOUND, 'Not Found'),
    ]
    archive = models.ForeignKey(
        'archive.Archive',
        on_delete=models.CASCADE,
    )
    metadata = JSONField()
    object_status = models.CharField(
        max_length=2,
        choices=FILE_STATUS,
        default=FOUND
    )
