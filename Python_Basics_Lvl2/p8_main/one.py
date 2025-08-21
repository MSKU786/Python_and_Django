def func(): 
  print("This is one.py func function")


print("One.py is initalized at top level")

if __name__ == '__main__':
  print("One.py is running directly")
else:
  print("one.py has been imported")