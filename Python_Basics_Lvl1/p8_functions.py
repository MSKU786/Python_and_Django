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

print();
print("Lambda Functions")

#Lambda Functions


#Filter
mylist = [1,2,3,4,5,6,7,8]

def even_bool(num):
  return num%2 == 0;

evens = filter(even_bool, mylist)

even_with_lambda = filter(lambda num:num%2==0, mylist)

print(list(evens));
print("Lambda implentation", list(even_with_lambda))

print('x' in [1,3,4,5,6])