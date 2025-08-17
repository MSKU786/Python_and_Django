try:
  f = open('simple.txt','r')
  f.write("Test write to simple text!")
except IOError:
  print('ERROR! COULD NOT FIND FILE OR READ DATA')
else:
  print("SUCCESS!")
  f.close()

print("other variation")

try:
  f = open('simple.txt','r')
  f.write("Test write to simple text!")
except:
  print('ERROR! COULD NOT FIND FILE OR READ DATA')
finally:
  print("FINAL BLOCK WILL ALWAYS WORK NO MATTER WHAT")
