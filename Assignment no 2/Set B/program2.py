string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
first1 = string1[:2]
first2 = string2[:2]
newstring1 = first2 + string1[2:]
newstring2 = first1 + string2[2:]
print(newstring1 + newstring2)
