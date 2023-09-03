
from django.urls import path, include
from . import views
from .views import MyTokenObtainPairView
from rest_framework.routers import DefaultRouter
from .views import receive_location_data
from .views import LocationDataDetailView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
# Create a DefaultRouter instance and register the GPSDataViewSet


urlpatterns = [
    path('receive-location/', receive_location_data, name='receive_location_data'),
    path('profile/', views.get_profile),
    path('location-data/', LocationDataDetailView.as_view(), name='location_data_detail'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  
]

