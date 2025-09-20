from django.forms import ModelForm
from AppTwo.models import User

class NewUserForm(ModelForm):
  class Meta:
    model = User
    fields = '__all__'