#program  to find out if the string contains: any alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
#any() checks a group and returns true if atleast one value in a group returns true
s=input("enter the string:")
print(any(char.isalnum()for char in s))
print(any(char.isalpha()for char in s))
print(any(char.isdigit()for char in s))
print(any(char.islower()for char in s))
print(any(char.isupper()for char in s))