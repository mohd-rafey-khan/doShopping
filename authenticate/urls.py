from django.urls import path, include
from authenticate import views

urlpatterns = [
    path('jwt/',include('authenticate.Router.jwtUrls')),
    path('product',views.Product,name="product doshopping"),
]