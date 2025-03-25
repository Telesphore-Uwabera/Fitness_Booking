from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, FitnessClassViewSet, BookingViewSet

router = DefaultRouter()
router.register(r'classes', FitnessClassViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', include(router.urls)),
]
