from django.shortcuts import render

# Create your views here.
from rest_framework_jwt.views import ObtainJSONWebToken

from .serializers import JWTSerializer
# Create your views here.
class ObtainJWTView(ObtainJSONWebToken):
    serializer_class = JWTSerializer
