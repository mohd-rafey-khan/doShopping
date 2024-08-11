from django.urls import path, include
from authenticate import views


urlpatterns = [
    path('/jwt/',views.JWT,name="JWT AUTH")
]