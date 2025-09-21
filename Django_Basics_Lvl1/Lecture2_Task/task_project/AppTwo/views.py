from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
from AppTwo.forms import NewUserForm
# Create your views here.
def index(request):
  return render(request, 'apptwo/index.html')


def help(request):
  my_dict = {"insert_me": "This is from my help page"}

  return render(request, 'apptwo/help.html', context=my_dict)

def users(request):
  # users_list = User.objects.order_by('email')
  # user_dict = {'users_records': users_list}
  # return render(request, 'apptwo/users.html', context=user_dict)
  form = NewUserForm()

  if (request.method == 'POST'):
    form = NewUserForm(request.POST)

    if form.is_valid():
      form.save(commit=True)
      return index(request)
    else:
      print("Error!! form is not valid")
  
  return render(request, 'apptwo/users.html', {'form': form})