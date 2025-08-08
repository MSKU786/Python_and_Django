def my_func(param1='default'):
  """
  This is the DOC string
  """
  print("This is first function {}".format(param1))
  return "Hello"


def addNum(num1, num2):
  return num1+num2;

def addNumTypeCheck(num1, num2):
  if (type(num1) == type(num2) == type(10)):
    return num1+num2
  else:
    return "Sorry, I need integers";
 
my_func();

result = my_func();
print(result);

result = addNum("2", "3")
print(result, type(result))

result = addNum(2,3)
print(result, type(result))

result = addNumTypeCheck("2", "3")
print(result, type(result))

result = addNumTypeCheck(2,3)
print(result, type(result))