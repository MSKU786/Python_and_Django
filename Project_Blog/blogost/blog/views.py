from django.shortcuts import render
from blog.models import Post,Comment
from django.views.generic import (TemplateView, ListView, DetailView, 
                                  CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixins
from blog.forms import PostForm
# Create your views here.


class AboutView(TemplateView):
  template_name = 'about.html'

class PostListView(ListView):
  model = Post

  def get_queryset(self):
    return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
  model = Post

class PostCreatetView(LoginRequiredMixins,CreateView):
  login_url = '/login/'
  redirect_field_name = 'blog/post_detail.html'

  form_class = PostForm
  model = Post


class PostUpdateView(LoginRequiredMixins,UpdateView):
  login_url = '/login/'
  redirect_field_name = 'blog/post_detail.html'

  form_class = PostForm
  model = Post


class PostDeleteView(LoginRequiredMixins, DeleteView):
  model = Post
  success_url = reverse_lazy('post_list')


class DraftListView(LoginRequiredMixins, ListView):
  login_url = '/login/'
  redirect_field_name = 'blog/post_list.html'

  model = Post

  def get_queryset(self):
    return Post.objects.filter(published_date_isnull=True).order_by('-created_date')
