string = 'thequickbrownfoxjumpsoverthelazydog'
counts = {} 
for char in string:
  if char in counts:
    counts[char] += 1 
  else:
    counts[char] = 1
for char in counts: 
  if counts[char] > 1:
    print(char, counts[char]) 
