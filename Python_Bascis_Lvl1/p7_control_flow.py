# Conitional Statments

if (1 < 2):
  print('Yes!!!')
  if (2 < 3): 
    print("Second Block!!!")
  else:
    print("Second block else block")
elif (3 < 5): 
  print("First block elif statement")


# For loops
seq = [1,3,4,6,7,8]
for s in seq:
  print(s);

dict = {"Sam":1, "Frank":2, "Dan": 3}
for key in dict:
  print(key)
  print(dict[key])

my_pairs = [(1,2),(2,3),(3,4),(4,5)]
for tup in my_pairs:
  print(tup);

for (tup1, tup2) in my_pairs:
  print(tup1);
  print(tup2);

# while loop
i = 1

while i<5: 
  print("i is:  {}".format(i));
  i += 1


# Range keyword
print(range(5))
print(list(range(5)))
print(list(range(0,20,4)))

for item in range(10):
  print(item);

# LIst comprehension
x = [1,2,3,4]

out = []
for num in x:
  out.append(num ** 2)

print(out);

out2 = [num**2 for num in x]
print(out2)