from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.chatrooms, name = 'chatrooms'),
    path('<slug:slug>/', views.chatroom, name = 'chatroom'),
]