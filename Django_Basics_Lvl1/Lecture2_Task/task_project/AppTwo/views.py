from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(req):
  return HttpResponse('<em>My Second App</em>')


def help(request):
  my_dict = {"insert_me": "This is from my help page"}

  return render(request, 'apptwo/help.html', context=my_dict)