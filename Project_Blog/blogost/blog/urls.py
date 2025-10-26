from django.conf.urls import url
from blog import views

urlpatterns = [
    path('/', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('about/', views.AboutView.as_view(),  name='about'),
    path('/post/new', views.PostCreateView.as_view(), name='new_post'),
    path('/post/<int:pk>/edit', view.PostUpdateView.as_view(), name='edit_post'),
    path('/post/<int:pk>/remove', view.PostDeleteView.as_view(), name='remove_post'),
    path('/drafts/', view.DraftListView.as_view(), name='post_draft_list')
]