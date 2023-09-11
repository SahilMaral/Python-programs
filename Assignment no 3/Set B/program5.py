my_tuple = (1, 2, 3, 4, 5, 3, 2, 1)
count = {}
for i in my_tuple:
  if i in count:
    count[i] += 1
  else:
    count[i] = 1
repeat = []
for key, value in count.items():
  if value > 1:
    repeat.append(key)
print(repeat)