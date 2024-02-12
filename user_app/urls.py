from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerUser, name="registerUser"),
    path('login/', views.loginUser, name="loginUser"),
    path('logout/', views.logoutUser, name="logoutUser"),
    path('view/user/<int:id>/', views.viewUser, name="view-user"),
    path('update/user/<int:id>/', views.updateUser, name="update-user"),




]
