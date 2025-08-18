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
  print(match.start())

  split_term = ','
  email = 'user@gmail.com,manish@gmail.com'
  print(re.split(split_term,email))


def multi_re_find(patterns, pharse):

  for pat in patterns:
    print(f"Searching for pattern {pat}")
    print(re.findall(pat, pharse))
    print("\n")

  
test_phrase = 'sdsd....sssddd...sddsdddd...dsds....dsssss...sddddd'

test_pattern = ['sd*, s*d']


multi_re_find(test_pattern, test_phrase)

