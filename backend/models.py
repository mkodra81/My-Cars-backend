from django.db import models
from django.contrib.auth.models import User
import os
from django.utils.timezone import now


def upload_to(instance, filename):
    ext = filename.split('.')[-1]
    return os.path.join('cars', f"{instance.id}_{int(now().timestamp())}.{ext}")


class Car(models.Model):
    """Car model for managing user vehicles"""
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cars')
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=50, blank=True, null=True)
    license = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.year} {self.brand} {self.model} - {self.license}"
