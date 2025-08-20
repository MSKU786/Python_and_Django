s = "GLOBAL VARIABLE!"

def func():
  mylocal = 10
  # return a dictioanry with all the local varaible of function
  print(locals())

   # return a dictioanry with all the gobal varaible
  print(globals())

func()