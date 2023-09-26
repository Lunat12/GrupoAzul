from django.urls import path
from . import views  # Asegúrate de tener un archivo views.py en tu aplicación

urlpatterns = [
    # Ejemplo de patrón de URL para una vista llamada 'index' en tu archivo views.py
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),  
]

