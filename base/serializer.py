from rest_framework import serializers
from base.models import *
from .models import GPSData

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'



class GPSDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPSData
        fields = '__all__'