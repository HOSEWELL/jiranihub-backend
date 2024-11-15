from django.db import models
from users.models import User  # Import User model
from issues.models import JiraniIssue  # Import Issue model
from announcements.models import Announcement  # Import Announcement model

class Notification(models.Model):
    notification_type = models.CharField(max_length=20)  # Issue or Announcement
    message = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")  # FK to User
    issue = models.ForeignKey(JiraniIssue, on_delete=models.CASCADE, null=True, blank=True, related_name="notifications")  # FK to Issue (optional)
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE, null=True, blank=True, related_name="notifications")  # FK to Announcement (optional)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username}"
