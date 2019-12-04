from django.core.validators import FileExtensionValidator
from django.db import models


class Document(models.Model):
    file = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)

    validate_file = FileExtensionValidator
