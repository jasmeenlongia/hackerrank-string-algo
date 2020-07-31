from collections import Counter

if len(Counter(input().lower())) == 27:
  print("pangram")
else:
  print("not pangram")
