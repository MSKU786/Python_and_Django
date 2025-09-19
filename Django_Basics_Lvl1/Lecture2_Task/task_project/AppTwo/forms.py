from django.forms import ModelForm
from AppTwo import models

class UserForm(ModelForm):
  class Meta:
    fields = ['first_name', 'last_name', "email"]