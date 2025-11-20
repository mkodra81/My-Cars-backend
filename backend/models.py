from django.db import models
from django.contrib.auth.models import User


class CarDetails(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Car Details"

    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"


class Car(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cars')
    car_details = models.ForeignKey(CarDetails, on_delete=models.CASCADE, related_name='cars')
    license = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.car_details} - {self.license}"
