from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from base.serializer import ProfileSerializer
from rest_framework import generics
from base.models import LocationData
from base.serializer import LocationDataSerializer
from rest_framework import status


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer




@api_view(['PUT'])  # You can also use 'PATCH' for partial updates
@permission_classes([IsAuthenticated])
def get_profile(request):
    user = request.user
    profile = user.profile

    # Serialize and update the profile data
    serializer = ProfileSerializer(profile, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx GPS xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
@api_view(['POST'])
def receive_location_data(request):
    try:
        latitude = request.data['latitude']
        longitude = request.data['longitude']
        build_number = request.data['buildNumber']

        # Save the received data to the database
        LocationData.objects.create(
            latitude=latitude,
            longitude=longitude,
            build_number=build_number,
        )

        return Response({'message': 'Location data received and stored successfully.'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class LocationDataDetailView(generics.RetrieveAPIView):
    queryset = LocationData.objects.all()
    serializer_class = LocationDataSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.profile.location_data