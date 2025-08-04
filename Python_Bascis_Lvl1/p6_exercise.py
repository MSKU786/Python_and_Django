s = 'django'

# Use indexing to print out following

# 'd'
print(s[0])

# 'o'
print(s[-1])

# 'djan'
print(s[:4])

# 'jan'
print(s[1:4])

# 'go'
print(s[4:])

#Bonuse: Use indexing to reverse the string
print(s[::-1])

# Use indexing to reverse the string


#Problem 2
l = [3, 7, [1,4 , 'hello']]

# Reassign hello to goodbye
l[2][2] = 'goodbye'
print(l);


#Problem 3;

# USing keys and indexing, grab the 'hello' from the following dictionaries:

d1 = {'simple_key': 'hello'}
d2 = {'k1': {'k2': 'hello'}}
d3 = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}

print(d3['k1'][0]['nest_key'][1][0]);


# Problem 4;
age = 4
name = "sammy"

# Use print formatting to print the following string
# "Hello my dog's name is sammy and he is 4 year old"

print("Hello my dog's name is {} and he is {} year old".format(name, age))