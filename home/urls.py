
from home import views
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.loginuser,name='login'),
    path('register',views.registeruser,name='register'),
    path('logout',views.logoutuser,name='logout'),
    path('play',views.play,name='play'),
]
