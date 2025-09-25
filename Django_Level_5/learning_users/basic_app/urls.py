from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from basic_app import views

# Template URL's

app_name = 'basic_app'

urlpatterns = [
  path('register', views.register, name='register'),
  path('login', views.login, name='login')
]