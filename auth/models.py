import uuid
from django.db import models
from datetime import datetime

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # UUID as primary key
    email = models.EmailField(max_length=30)
    username = models.CharField(max_length=30)
    phone_no = models.CharField(max_length=15)  # Use CharField for phone numbers
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    status = models.BooleanField(default=True)  # Set a default value for status
    deleted_at = models.DateTimeField(null=True, blank=True, default=None)  # Allow deleted_at to be null

    def __str__(self):
        return self.id


class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # UUID as primary key
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')  # Relationship to User
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    last_login = models.DateTimeField(default=datetime.now)
    # profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)  # Field for profile picture

    def __str__(self):
        return self.id
