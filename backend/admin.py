from django.contrib import admin
from .models import Car, CarDetails


@admin.register(CarDetails)
class CarDetailsAdmin(admin.ModelAdmin):
    list_display = ['id', 'brand', 'model', 'year', 'color']
    search_fields = ['brand', 'model']
    list_filter = ['brand', 'year']


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['id', 'license', 'car_details', 'owner', 'created_at']
    search_fields = ['license', 'car_details__brand', 'car_details__model', 'owner__username']
    list_filter = ['created_at', 'car_details__brand']
    raw_id_fields = ['owner', 'car_details']

