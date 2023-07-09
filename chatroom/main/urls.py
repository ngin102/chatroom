from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.mainpage, name = 'mainpage'),
    path('signup/', views.signup, name = 'signup'),
    path('signin/', auth_views.LoginView.as_view(template_name = 'signin.html'), name = 'signin'),
    path('signout/', auth_views.LogoutView.as_view(), name = 'signout')
]