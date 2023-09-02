
from django.urls import path, include
from . import views
from .views import MyTokenObtainPairView
from rest_framework.routers import DefaultRouter


from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
# Create a DefaultRouter instance and register the GPSDataViewSet


urlpatterns = [
    path('profile/', views.get_profile),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  
]

