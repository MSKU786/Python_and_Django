s = "GLOBAL VARIABLE!"

def func():
  mylocal = 10
  # return a dictioanry with all the local varaible of function
  print(locals())

   # return a dictioanry with all the gobal varaible
  print(globals())

func()


# Assign funciton to a variable

def hello(name = 'Ajay'):
  return 'Helloooo.... '+ name

print(hello())

my_new_greet = hello
print(my_new_greet())



def outer_function(param = 'first'):
  print("The outer function has been revoked")
  def inner():
    print("I am inside inner function")
  def inner2():
    print("I am inside inner 2 function")
  
  if param == 'first':
    return inner
  else:
    return inner2
  print("End of outer function")

# if you try to call this directly it will throw error
#inner()


x = outer_function();

print(x())



# Passing funciton as parament

def greet():
  return "Hi Shubham"

def other(func):
  print("hello")
  print(func())

other(greet())