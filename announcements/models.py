# announcements/models.py

from django.db import models
from users.models import User

class Announcement(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='announcements/', null=True, blank=True)  # New field

    def __str__(self):
        return self.title
