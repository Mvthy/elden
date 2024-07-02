from django.urls import path
from  . import views

urlpatterns = [
    path('Home', views.home, name='Home'),
    path('Quienes-somos', views.QuieneSomos, name='Quienes-somos'),
    path('Servicios', views.servicios, name='Servicios'),
]