from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.user.username



class GPSData(models.Model):
    module_identifier = models.PositiveIntegerField(
        unique=True,
        null=True,
        blank=True
    )
    asset_name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=14, decimal_places=12)
    longitude = models.DecimalField(max_digits=14, decimal_places=12)
    altitude = models.DecimalField(max_digits=14, decimal_places=12)
    speed = models.DecimalField(max_digits=14, decimal_places=9)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"GPS Data - Module: {self.module_identifier}, Lat: {self.latitude}, Lon: {self.longitude}, Alt: {self.altitude}, Speed: {self.speed}, Time: {self.timestamp}"
