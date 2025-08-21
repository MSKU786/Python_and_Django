import one

print("Two.py is initialzed at top level")

one.func()

if __name__ == '__main__':
  print("Two.py is running directly")
else:
  print("Two.py has been imported")