my_list = [1,2,3,8,7,6,5,4]

# List can contain different types of data
my_list2 = ['stadfa',1,23.3, True, [1,23,4]]
print(len(my_list2));
print(my_list2[0]);
print(my_list2);
# Unlink strings list are muttable
 
my_list2[0] = 'new_value';
print(my_list2);

my_list2.append(20);
print(my_list2);

my_list2.extend([1,2,3]);
print(my_list2);

# In pop we can specify the index of the item to remove
item = my_list2.pop();
print(my_list2);
print(item);  


my_list.sort();
print(my_list);

matrix = [[1,2,3], [4,5,6], [7,8,9]]

#List Comprehension

first_col = [row[0] for row in matrix]
print(first_col);