####################
### Game Project ### 
####################

# Conditions
# The computer will think of 3 digit numbe rhtat has no re3peeating digts. 
# You will then guess a 3 digit number
# The compute will then give bacvk clues. 
# Basewd on these cluses you wil guess again until you break the code with a match

# Clues
# Close: You've guewssed a correct number but itn thte wrong position
# Match: You've guessed a correct number int he correct position
# Nope: You haven't guess any of the numbers correctly

import random

print("Welcome Code Breaker! Let's see if you can guess my 3 digit number!")
print("Code has been generated, please guess a 3 digit number")


def generate_random():
  a = random.randint(0,9)
  b = random.randint(0,9)
  while (b == a):
    b = random.randint(0,9)
  c = random.randint(0,9)
  while ( a==c or b==c ):
    c = random.randint(0,9)
  
  return [c,b,a]



def check_user_input(ans):
  print(ans)
  num = int(input(("What is your guess? ")))
  if (num>999 or num < 100):
    print("Only 3 digits of numbers are valid")
    check_user_input()
    return;
  a = num%10;
  num = num//10;
  b = num%10
  num = num//10
  c = num%10
  num = num//10

  if (ans[0] == c and ans[1] == b and ans[2] ==a):
    print("Great! You won the game :) .......")
    return;

  clue = ''
  if (a in ans or b in ans or c in ans):
    clue = 'Close'
  
  if (ans[0] == c or ans[1] == b or ans[2] == a):
    clue = 'Match'
  
  if (clue == ''):
    clue = 'Nope'

  print(clue)
  check_user_input(ans);

ans = generate_random();
check_user_input(ans);