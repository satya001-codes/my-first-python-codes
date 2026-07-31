#program  to find out if the string contains: any alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
s=input("enter the string:")
has_alnum=has_alpha=has_digit=has_upper=has_lower=False
for char in s:
    if char.isalnum():
        has_alnum=True
    if char.isalpha(): 
        has_alpha=True
    if char.isdigit():
        has_digit=True
    if char.isupper():
        has_upper=True
    if char.islower():
        has_lower=True

print(has_alnum)
print(has_alpha)         
print(has_digit)
print(has_upper)
print(has_lower)              