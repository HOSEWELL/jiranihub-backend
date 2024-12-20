from django.db import models
from users.models import User  

class JiraniIssue(models.Model):
    name = models.CharField(max_length=255)  # Name of the issue
    issue = models.TextField()  # Detailed description of the issue
    contact_info = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=20, default="pending")  # status: pending, resolved
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="issues")  # FK to User

    def __str__(self):
        return self.name  # Return name of the issue
