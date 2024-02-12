from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerUser, name="registerUser"),
    path('login/', views.loginUser, name="loginUser"),
    path('logout/', views.logoutUser, name="logoutUser"),




]
