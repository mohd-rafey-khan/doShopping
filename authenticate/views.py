from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .Auth.Register import Register
from .Auth.Controller.register.JwtRegisterUser import JwtRegisterUser
from .Auth.Controller.register.OauthRegisterUser import OauthRegisterUser
from .Auth.Login import Login
from .Auth.Controller.login.JwtLoginUser import JwtLoginUser
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken
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


@api_view(['POST'])
@permission_classes([AllowAny])
def LoginUser(request):
    data = request.data

    user_login = Login()
    user = user_login.login(JwtLoginUser(data))

    reseponse = ""

    if user is not None:
        if request:
            # Log the user in using the request object
            login(request, user)

            # Generate JWT token
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            # Return the token in the response
            reseponse =  {
                'access': access_token,
                'refresh': str(refresh)
            }
        else:
            reseponse =  {
                'message': "Request object is missing."
            }
    else:
        reseponse =  {
            'message': "Invalid Credentials"
        }

    return Response(reseponse)