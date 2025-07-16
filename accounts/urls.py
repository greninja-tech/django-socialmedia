"""
URL configuration for socialmedia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from accounts.views import registration,login_view,home
from . import views

urlpatterns = [
    path('',registration, name='register'),
    path('login_view/',login_view, name='login'),
    path('profile/<int:user_id>/',views.profile_view,name='profile'),
    path('follow/<int:user_id>/', views.toggle_follow, name='toggle_follow'),
    path('home/', home, name='home'),
    path('logout/', views.logout_view, name='logout'),
]
