from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from doShopping.helper.responses import Response



# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def masterInsert(request, type):

    reseponse =  {
            'message': type
        }

    return Response.success(data=reseponse, message='werty')
