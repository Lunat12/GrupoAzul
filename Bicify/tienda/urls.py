from django.urls import path, re_path
from . import views  

urlpatterns = [
    path('index/<pk>', views.index, name='index'),
    path('accesories/', views.accesories, name='accesories'),
    path('register/', views.register, name='register'),
    #path('login/',views.login,name='login'),
    path('profile/',views.profile,name='profile'),
]