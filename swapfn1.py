#ASCII method to built swap fuction from scratch 
def swap_keepsymbols(text):
    result="" #an empty string
    for char in text:
        a=ord(char) # find the ascii value :upeercase-65 to 90 ; lowercase-97to 122
        if a>=65 and a<=90:  
            result += chr(a+32)  #why the 32? the difference between uppercase and lowercase ascii value is 32
        elif a>=97 and a<=122:
            result += chr(a-32)
        else:
            result+=char #symbols,letters and spaces unchanged
    return result        

def swap_removesymbols(text):
    result="" #an empty string
    for char in text:
        a=ord(char) # find the ascii value :upeercase-65 to 90 ; lowercase-97to 122
        if a>=65 and a<=90:  
            result += chr(a+32)  #why the 32? the difference between uppercase and lowercase ascii value is 32
        elif a>=97 and a<=122:
            result += chr(a-32)
        else:
            pass
    return result        

def swap_replacesymbols(text):
    result="" #an empty string
    for char in text:
        a=ord(char) # find the ascii value :upeercase-65 to 90 ; lowercase-97to 122
        if a>=65 and a<=90:  
            result += chr(a+32)  #why the 32? the difference between uppercase and lowercase ascii value is 32
        elif a>=97 and a<=122:
            result += chr(a-32)
        else:
            result+="*"
    return result        


#test the functions
print("original version:",swap_keepsymbols("PyThoN 3.12"))
print("modified version:",swap_removesymbols("PyThoN 3.12"))
print("another modified version:",swap_replacesymbols("PyThoN 3.12"))