from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .Auth.Register import Register
from .Auth.Controller.JwtRegisterUser import JwtRegisterUser
from .Auth.Controller.OauthRegisterUser import OauthRegisterUser
# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def Product(request):
    return Response({"message": "This is a protected view!"})

@api_view(['POST'])
@permission_classes([AllowAny])
def RegisterUser(request):
    data = request.data
    userRegister = Register()
    userRegister.register(JwtRegisterUser(data))
    userRegister.register(OauthRegisterUser())
    return Response({"message": "User is registered"})