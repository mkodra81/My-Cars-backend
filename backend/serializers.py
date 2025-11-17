from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

from .models import Car
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_superuser', 'first_name', 'last_name', 'date_joined']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name',]


    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, validators=[validate_password])


class CarSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    permissions = [IsAuthenticated]

    class Meta:
        model = Car
        fields = ['id', 'owner', 'brand', 'model', 'color', 'year', 'license', 'created_at', 'updated_at']

