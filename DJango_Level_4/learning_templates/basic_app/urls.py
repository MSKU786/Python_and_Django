from django.urls import path
from basic_app import views

#Template Tagging
app_name = 'basic_app'

url_patterns = [
  path('relative/', views.relative, name = 'relative'),
  path('other/', views.other, name = 'other')
]