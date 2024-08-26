from django.db import models
from datetime import datetime

class ContentMaster(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    deleted_at = models.DateTimeField(null=True, blank=True, default=None)

    def __str__(self):
        return f"{self.id}: {self.name}"

class CommonMasterFormData(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    deleted_at = models.DateTimeField(null=True, blank=True, default=None)
    type = models.ForeignKey(ContentMaster, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}: {self.name}"
