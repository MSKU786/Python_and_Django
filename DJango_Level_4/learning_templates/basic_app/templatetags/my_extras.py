from django import template

register = template.Library()

def cut(value, args): 
  """
  This cut's out all the value of args 
  """

  return value.replace(args,'')

register.filter('cut', cut)