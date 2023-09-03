sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
item = 11
low = 0
high = len(sorted_list) - 1
found = False
while low <= high and not found:
  mid = (low + high) // 2
  if item == sorted_list[mid]:
    found = True
    print("Item ",item," is found at index ",mid)
  elif item < sorted_list[mid]:
    high = mid - 1
  else:
    low = mid + 1
if not found:
  print("Item ",item," is not found in the list")
