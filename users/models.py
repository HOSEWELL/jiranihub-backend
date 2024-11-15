from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('chief', 'Chief'),
        ('public', 'Public'),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    # Custom related_name to avoid clashes with the default User model
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Custom related_name to avoid conflict with the default User model
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='custom_user'
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',  # Custom related_name to avoid conflict with the default User model
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='custom_user_permission'
    )

    def __str__(self):
        return self.username
