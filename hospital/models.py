from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('client', 'Client'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='client')

    def is_admin(self):
        return self.user_type == 'admin'
    
    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.user_type = 'admin'
        super().save(*args, **kwargs)
