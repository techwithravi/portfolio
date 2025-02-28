from django.urls import path, include
from .views import UserRegisterView
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('user_logout', views.user_logout, name='logout'),

]

