#building a function from scratch to swap cases
def swapcase_keepsymbols(text):
    result=[] #an empty list
    for char in text:
        if char.isupper():
            result.append(char.lower())
        elif char.islower():
            result.append(char.upper())
        else:
            result.append(char) #keeps spaces,numbers and symbols as they are!    
    return "".join(result)

def swapcase_removesymbols(text):
    result=[]
    for char in text:
        if char.isupper():
            result.append(char.lower())
        if char.islower():
            result.append(char.upper())
        else:
            pass  #removes them 
    return "".join(result)

def swapcase_replacesymbols(text):
    result=[]
    for char in text:
        if char.isupper():
            result.append(char.lower())
        if char.islower():
            result.append(char.upper())
        else:
            result.append("*")
    return "".join(result)        


#test the functions
print("original version:",swapcase_keepsymbols("PyThoN 3.12"))
print("modified version:",swapcase_removesymbols("PyThoN 3.12"))
print("another modified version:",swapcase_replacesymbols("PyThoN 3.12"))