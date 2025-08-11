# Python Scopes follow the LEGB Rule
# - Local
# - Enclosing function call
# - Global
# - Built In

# Local: Names Assigned in a way within a function (def and lambda), and not declared global in that function
# EFLs: Name in the local scope of any and all encloing functions (def or lambda), from inner to outer.
# Globa: Names assinged at the top level of module, file or declared global in the def within the file.
# Built-in: Names preassinged in the build in module. Ex: open, range, SyntaxError

x = 25

def my_func():
  x = 50;
  #print(x)
  return x;

print(x);
print(my_func());
print(x);


# Enclosing funciton locals

name = 'This is global name!'

def greet():
  name = 'sammy'

  def hello():
    print("hello "+name)

  hello()

greet();
print(name);


x = 50

def func():
  global x
  x = 100

print("Before function call x is ", x);
func();
print("After function x is ", x);