#Program to capitalize the first word of first and last name 
def solve(s):
    full=s.split() #how split works and its syntax:anything.split("separator about which we have to split(default-splits around space)")
    char_f=list(full[0]) #extracts the first name and converts them into a list which contains every character separately
    char_l=list(full[1]) #extracts the last name and converts them into a list which contains every character separately
    char_f[0]=char_f[0].upper() #accessed the first character of the first name and capitalized it
    char_l[0]=char_l[0].upper() #accessed the first character of the last name and capitalized it
    #joined the characters and made the changes to the original list
    full[0]="".join(char_f) 
    full[1]="".join(char_l)
    #joined the first and last name with a space 
    return " ".join(full)
  

#But,This program is restricted only to name with two words(first and last) fails when there is a middle name(it produces the output but not the required one)
#In case of single name - it does not produce the output even
#Another problem is that using split without argument(separator about which we have to split) ignores multiple spaces


#fixing the problems using capitalize function 
#capitalize function changes the first letter to uppercase and all other to lowercase
def solve_universal(s):
    words=s.split(" ") #splitting around space
    c=[word.capitalize() for word in words]
    return " ".join(c)


#this case also fails when in input there is a word with pre-existing uppercase letters in the middle(like:McDonalds,iPhone)


#test the code
if __name__=="__main__":
    s=input("enter the name:")
    print("modified version:",solve_universal(s))
    print("original version:",solve(s))
    

