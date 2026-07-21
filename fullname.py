#program to read the firstname and lastname of a person on two different lines and print the following:Hello firstname lastname! You just delved into python.
#input format:The first line contains the first name, and the second line contains the last name.
#using f-string and directly printing within the function
def print_full_name(first,last):
    print(f"Hello {first} {last}! You just delved into python.")


#using f-string but not, directly printing it within the function.Instead,returning the text to the function
def full_name(first,last):
    return f"Hello {first} {last}! You just delved into python."


#using list 
def list_full_name(first,last):
    name=[]
    name.append("Hello ")
    name.append(first)
    name.append(" ")
    name.append(last)
    name.append("! You just delved into python.")
    message ="".join(name)
    print(message)


#test the function
if __name__=="__main__":
    first_name=input("enter the first name:")
    last_name=input("enter the last name:")
    print("original version:",end=" ")
    print_full_name(first_name,last_name)
    print("modified version(1):",full_name(first_name,last_name))
    print("modified version(2):",end=" ")
    list_full_name(first_name,last_name)
