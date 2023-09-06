from django.db import models
from django.contrib.auth.models import User
from django.db import models


class LocationData(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    build_number = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.latitude}, {self.longitude} ({self.build_number})"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    location_data = models.OneToOneField(LocationData, on_delete=models.CASCADE, related_name='profile', null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    def __str__(self):
        return self.user.username
