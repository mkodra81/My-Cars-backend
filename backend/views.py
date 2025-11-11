from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from .models import Car
from .serializers import (
    UserSerializer,
    RegisterSerializer,
    CarSerializer,
    ChangePasswordSerializer
)
from rest_framework.decorators import action


# ==========================
# User ViewSet (Registration & Account Management)
# ==========================
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


    def get_serializer_class(self):
        if self.action == 'create':
            return RegisterSerializer
        return UserSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [IsAuthenticated()]

    def create(self, request, *args, **kwargs):
        """Register a new user"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        """Delete user account - only the account owner can delete their own account"""
        user = self.get_object()
        if user != request.user and not request.user.is_staff:
            return Response({"detail": "Not authorized to delete this account."}, status=status.HTTP_403_FORBIDDEN)
        user.delete()
        return Response({"detail": "Account deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


# ==========================
# Get Current User
# ==========================
class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


# ==========================
# Change Password
# ==========================
class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user
        if not user.check_password(serializer.validated_data['old_password']):
            return Response({"old_password": "Incorrect password."}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(serializer.validated_data['new_password'])
        user.save()
        return Response({"detail": "Password updated successfully."})


# ==========================


# ==========================
# Car ViewSet (CRUD)
# ==========================
class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Car.objects.all().order_by('-created_at')
        return Car.objects.filter(owner=user).order_by('-created_at')

    @action(detail=False, methods=['post'], url_path='owner/(?P<owner_id>[^/.]+)', permission_classes=[IsAdminUser])
    def create_for_owner(self, request, owner_id=None):
        """Create a car for a specific owner - staff only"""
        try:
            owner = User.objects.get(id=owner_id)
        except User.DoesNotExist:
            return Response({"detail": "Owner not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=owner)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        car = self.get_object()
        if car.owner != self.request.user and not self.request.user.is_staff:
            return Response({"detail": "Not authorized to update this car."}, status=status.HTTP_403_FORBIDDEN)
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        car = self.get_object()
        if car.owner != request.user and not request.user.is_staff:
            return Response({"detail": "Not authorized to delete this car."}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)
