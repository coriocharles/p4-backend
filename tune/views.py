from .serializer import CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework.parsers import MultiPartParser, FormParser

class CustomTokenObtainPairView(TokenObtainPairView):
    # Replace the serializer with your custom
    serializer_class = CustomTokenObtainPairSerializer
