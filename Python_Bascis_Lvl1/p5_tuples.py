# Tuples are immutable sequence
# Sets are unordered collection of unique elements
# Boolean are True and False as other languages

#Booleans
boolean = [True, False, 0, 1];


#Tuples
t = (1,3,4,6);
print(t[0]);

# Can't change the values like list they can hold mutiple datatype 
tup = (3,"adf",23.43,[1,3]);

print(tup);


#sets
x = set();
x.add(1)
x.add(2)
x.add(2)
x.add(3)
x.add(2)
print(x);

listToSet = set([1,34,2,1,1,1,3,34,2,34,3,4,6])
print(listToSet)