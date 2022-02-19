from django.urls import path, include
from projects import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('newproject/', views.newproject, name='newproject'),
]