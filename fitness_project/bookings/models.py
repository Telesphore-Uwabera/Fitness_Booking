from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_trainer = models.BooleanField(default=False)

class FitnessClass(models.Model):
    name = models.CharField(max_length=255)
    trainer = models.ForeignKey(User, on_delete=models.CASCADE)
    schedule = models.DateTimeField()

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fitness_class = models.ForeignKey(FitnessClass, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} booked {self.fitness_class.name}"
