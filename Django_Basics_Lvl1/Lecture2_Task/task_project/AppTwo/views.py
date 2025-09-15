from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
# Create your views here.
def index(req):
  return HttpResponse('<em>My Second App</em>')


def help(request):
  my_dict = {"insert_me": "This is from my help page"}

  return render(request, 'apptwo/help.html', context=my_dict)

def users(request):
  users_list = User.objects.order_by('email')
  user_dict = {'users_records': users_list}
  return render(request, 'apptwo/users.html', context=user_dict)