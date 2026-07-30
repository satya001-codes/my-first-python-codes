#program  to find out if the string contains: any alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
#using list method and shortening te code length
s=input("enter the string:")
methods=[str.isalnum,str.isalpha,str.isdigit,str.isupper,str.islower]
for method in methods:
    print(any(method(char) for char in s)) 
