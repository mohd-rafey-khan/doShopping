from django.urls import path, include
from authenticate import views

# JWT
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('jwt/api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt/api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]