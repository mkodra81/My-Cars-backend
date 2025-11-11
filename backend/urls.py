from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, MeView, ChangePasswordView, CarViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('cars', CarViewSet, basename='cars')

urlpatterns = [
    path('me/', MeView.as_view(), name='current-user'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('', include(router.urls)),
]
