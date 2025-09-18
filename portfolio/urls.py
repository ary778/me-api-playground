# portfolio/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, HealthCheckView

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'profile', ProfileViewSet, basename='profile')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('health/', HealthCheckView.as_view(), name='health-check'),
]