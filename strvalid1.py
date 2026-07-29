#program  to find out if the string contains: any alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
# map(function,iterable) applies a specific action to every item in a collection
s=input("enter the string:")
print(any(map(str.isalnum,s))) #str.isalnum is passed without parenthesis() ,because it is passed as an object not as a function
print(any(map(str.isalpha,s)))
print(any(map(str.isdigit,s)))
print(any(map(str.islower,s)))
print(any(map(str.isupper,s)))