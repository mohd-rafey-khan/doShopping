from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to the core User model
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    last_login = models.DateTimeField(default=datetime.now)
    phone_no = models.CharField(max_length=15, default='N/A')  # Provide a default value
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    status = models.BooleanField(default=True)
    deleted_at = models.DateTimeField(null=True, blank=True, default=None)
    role = models.CharField(max_length=50)  # Add role field with choices

    def __str__(self):
        return str(self.user.id)

