from django.urls import path, include
from AdminProduct import views

urlpatterns = [
    path('master/<int:type>', views.masterInsert, name='master'),
]