#a function to mutate string as it is an immutable form by changing it into a list(mutable)
def mutate_string(string,position,character):
    l=list(string)
    l[position]=character
    return "".join(l)

#input format-The first line contains a string.the next line contains an integer position(the index location) and a string character, separated by a space.
if __name__=="__main__":
    str=input("enter the string:")
    i, c=input("enter the required information:").split()
    new_str=mutate_string(str,int(i),c)
    print(new_str)
