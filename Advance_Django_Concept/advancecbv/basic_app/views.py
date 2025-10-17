from django.shortcuts import render
from django.db import models
from django.views.generic import View, TemplateView, ListView, DetailView
# from django.http import HttpResponse
# # Create your views here.
# def index(request):
#   return render(request, 'index.html')

# class CBView(View):
#   def get(self, request): 
#     return HttpResponse("Class based views are hard to implement")

# class IndexView(TemplateView):
#   template_name = 'index.html'

#   def get_context_data(self, **kwargs):
#     context= super().get_context_data(**kwargs)
#     context['injectme'] = 'BASIC INJECTION'
#     return context

class SchoolListView(ListView):
  context_object_name = 'schools'
  model = models.School
  # school_list 

class SchoolDetailView(DetailView):
  context_object_name = 'school_detail'
  model = models.School
  template_name = 'basic_app/school_details.html'