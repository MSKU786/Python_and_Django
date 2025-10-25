from django.conf.urls import url
from blog import views

urlpatterns = [
    path('/', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('about/', views.AboutView.as_view(),  name='about'),

]