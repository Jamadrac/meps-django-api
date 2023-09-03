from rest_framework import serializers
from base.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'




class LocationDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationData
        fields = ['latitude', 'longitude', 'build_number', 'timestamp']