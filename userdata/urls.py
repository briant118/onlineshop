from django.urls import path
from . import views

urlpatterns = [
    path('authentication/logout/', views.logout, name='logout'),
    path('userprofile/register/', views.register, name='register'),
    path('authentication/login/', views.login, name='user_login'),
]