from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.signup, name = 'signup'),
    path('chatrooms/', include('room.urls')),
    path('signup/', views.signup, name = 'signup'),
    path('signin/', auth_views.LoginView.as_view(template_name = 'signin.html'), name = 'signin'),
    path('signout/', auth_views.LogoutView.as_view(), name = 'signout')
]