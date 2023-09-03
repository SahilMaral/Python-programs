mydict = {'name':'abc','city':'xyz','country':'def'}
name = input("Enter a name of key dictonary: ")
if name in mydict:
  print('Key exists')
else:
  print('Key does not exist')