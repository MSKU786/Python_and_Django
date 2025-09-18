from django import forms
from django.core import validators


def check_for_z(value):
  if (value[0].lower() != 'z'):
    raise forms.ValidationError("Name should start with char `z`")
class FormName(forms.Form):
  name = forms.CharField(validators=[check_for_z])
  email = forms.EmailField()
  verify_email = forms.EmailField(label="Verify your email again")
  text = forms.CharField(widget=forms.Textarea)

  def clean(self):
    all_clean_data = super().clean();
    email = all_clean_data['email']
    vemail = all_clean_data['verify_email']

    if email != vemail:
      raise forms.ValidationError("Make sure emails are same")

  # def clean_bot_catcher(self):
  #   botcatcher = self.cleaned_data['bot_catcher']
  #   if (len(botcatcher) > 0):
  #     raise forms.ValidationError("Gotcha Bot!!!")
  #   return botcatcher
  

  
