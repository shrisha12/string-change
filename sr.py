import re
print("enter the string:")
str = input()
print("original string:")
print(str)
print(" After removing the upper case letters,above string is:")
remove_upper =lambda text: re.sub('[A-Z]', '',text)
result = remove_upper(str)
print(result)
