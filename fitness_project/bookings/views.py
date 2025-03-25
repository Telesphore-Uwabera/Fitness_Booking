from rest_framework import generics, viewsets
from django.contrib.auth import get_user_model
from .models import FitnessClass, Booking
from .serializers import UserSerializer, FitnessClassSerializer, BookingSerializer
from .utils import send_booking_confirmation

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FitnessClassViewSet(viewsets.ModelViewSet):
    queryset = FitnessClass.objects.all()
    serializer_class = FitnessClassSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        booking = serializer.save()
        send_booking_confirmation(booking.user.email, booking.fitness_class.name, booking.fitness_class.schedule)
