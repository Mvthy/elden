from django.urls import path , include
from . import views


urlpatterns = [
    path('Home/', views.Home, name="Home"),
    path('Quienes-somos/', views.QuieneSomos, name="Quienes-Somos"),
    path('Servicios/', views.Servicios, name="Servicios"),
]