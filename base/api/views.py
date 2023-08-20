from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from base.serializer import ProfileSerializer
from rest_framework import viewsets
from base.models import GPSData
from base.serializer import GPSDataSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

from rest_framework import status
from rest_framework.response import Response

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



# class GPSDataViewSet(viewsets.ModelViewSet):
#     queryset = GPSData.objects.all()
#     serializer_class = GPSDataSerializer



class GPSDataViewSet(viewsets.ModelViewSet):
    serializer_class = GPSDataSerializer

    def get_queryset(self):
        # Filter the queryset to retrieve GPS data only for the authenticated user
        user = self.request.user  # Assuming you have authentication set up correctly
        return GPSData.objects.filter(user=user)

# Manually specify the basename for the viewset
gps_data_viewset = GPSDataViewSet.as_view({'get': 'list', 'post': 'create'})

# You can choose a meaningful basename, for example, 'gpsdata'