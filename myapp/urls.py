from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('loginform/', views.loginform, name='loginform'),
    path('signupform/', views.signupform, name='signupform'),
    path('signupaction', views.signupaction, name='signupaction'),
    path('loginaction', views.loginaction, name='loginaction')
]
