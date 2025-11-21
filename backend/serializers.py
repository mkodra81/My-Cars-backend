from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

from .models import Car, CarDetails
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_superuser', 'first_name', 'last_name', 'date_joined']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'date_joined']


    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, validators=[validate_password])


class CarDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarDetails
        fields = ['id', 'brand', 'model', 'year', 'color']


class CarSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    permissions = [IsAuthenticated]
    car_details = CarDetailsSerializer()

    # Expose car_details fields at the top level for easier access
    brand = serializers.CharField(source='car_details.brand', read_only=True)
    model = serializers.CharField(source='car_details.model', read_only=True)
    year = serializers.IntegerField(source='car_details.year', read_only=True)
    color = serializers.CharField(source='car_details.color', read_only=True, allow_null=True)

    class Meta:
        model = Car
        fields = ['id', 'owner', 'car_details', 'brand', 'model', 'color', 'year', 'license', 'created_at', 'updated_at']

    def create(self, validated_data):
        car_details_data = validated_data.pop('car_details')
        car_details = CarDetails.objects.create(**car_details_data)
        car = Car.objects.create(car_details=car_details, **validated_data)
        return car

    def update(self, instance, validated_data):
        car_details_data = validated_data.pop('car_details', None)

        if car_details_data:
            # Update car_details
            for attr, value in car_details_data.items():
                setattr(instance.car_details, attr, value)
            instance.car_details.save()

        # Update car
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

