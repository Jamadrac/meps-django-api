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



class LocationDatataSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationData
        fields = '__all__'