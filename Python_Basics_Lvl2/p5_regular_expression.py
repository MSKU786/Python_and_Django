import re

patterns = ['term1', 'term2']

text = 'This is a string with term1, not the other1'

for pattern in patterns:
  print("I am searching for: "+pattern)

  if re.search(pattern, text):
    print("MATCH")
  else:
    print("NOT MATCHED")
  
  match = re.search(pattern, text)
  #print(match.start)

  split_term = ','
  email = 'user@gmail.com,manish@gmail.com'
  print(re.split(split_term,email))


def multi_re_find(patterns, pharse):

  for pat in patterns:
    print(f"Searching for pattern {pat}")
    print(re.findall(pat, pharse))
    print("\n")

  
test_phrase = 'sdsd....sssddd...sddsdddd...dsds....dsssss...sddddd'

# Quantifier and character class examples
test_pattern = [
  'sd*',      # 's' followed by zero or more 'd' characters
  's*d',      # zero or more 's' characters followed by a 'd' (so just 'd' also matches)
  'sd{3}',    # 's' followed by exactly 3 'd' characters (e.g., 'sddd')
  'sd{1,3}',  # 's' followed by between 1 and 3 'd' characters (inclusive)
  's[sd]+',   # 's' followed by one or more characters that are either 's' or 'd'
]


multi_re_find(test_pattern, test_phrase)

test_phrase_2 = 'This is a string! But it has punctuation. How we can remove it'

test_pattern = ['[^!.?]+', '[a-z]+', '[A-Z]+']  # one or more characters that are not '!', '.', or '?'
multi_re_find(test_pattern, test_phrase_2)
