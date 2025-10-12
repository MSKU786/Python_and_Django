from django.shortcuts import render
from django.views.generic import View, Template View
# from django.http import HttpResponse
# # Create your views here.
# def index(request):
#   return render(request, 'index.html')

# class CBView(View):
#   def get(self, request): 
#     return HttpResponse("Class based views are hard to implement")

class IndexView(TemplateView):
  template_name = 'index.html'

  def get_context_data(self, **kwargs):
    context= super().get_context_data(**kwargs)
    context['injectme'] = 'BASIC INJECTION'
    return context
