### Given a list of intergers, return true if sequence of 1,2,3 appears in the list somewhere

def arrayCheck(nums):
  unique_list = list(set(nums))
  if ( 1 in unique_list and 2 in unique_list and 3 in unique_list):
    return True
  else:
    return False
  
def arrayCheckSequence(nums):
  for i in range(len(nums)-2):
    if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
      return True;
  return False;

# Given a string, return a new string made of every other charcter startign with the first so "Hello" yields "hlo"
# stringBits('Hello) => 'Hlo
# stringBits('Hlo') => 'H'

def stringBits(str): 
  ans = ''
  for i in range(len(str)):
    if (i%2 ==0):
      ans+=str[i];
  return ans

print(stringBits('Hello'))
print(stringBits('Hlo'))


# Given two string return True if either of the string  appears at the end of the other string
# end_other("Hlabc",'abc') => True
# end_other('AbC', 'HiaBc') => True

def end_other(a, b):
  #optional
  # a[-len(b)].lower() == b.lower() or b[-len(a)].lower() == a.lower(); 
  return ( a[-min(len(a), len(b)):].lower() == b[-min(len(a), len(b)):].lower());

print(end_other("Hlabc",'aBc'));
print(end_other('AbC',"hiabcd"));


# Given a string return a string whree for every char in the orignal, there are two chars
# doubleChars('The') -> 'TThhee'
# doubleChars('AAbb') -> 'AAAAbbbb'

def doubleChars(str):
  ans = ''
  for a in str:
    ans += 2*a
  return ans;

print(doubleChars('The'))
print(doubleChars('AAbb'))


## Return number of even integers in an array
 
def count_evens(nums):
  count = 0
  for num in nums:
    if (num%2==0): 
      count+=1
  
  return count

print(count_evens([1,2,3,4,5,67,87]));
print(count_evens([1,1,1,1,3,3,3,3,4]))