#a function to Split the string on a " " (space) delimiter and join using a - hyphen.
def split_and_join(line):
    for char in line:
        a=line.split()
    return "-".join(a) 
   

#improvement: 'for' is not necessary, the split function can do that same work then why to repeat it  
def split_and_join1(line):
        a=line.split() 
        return "-".join(a) 


#applying manual loop logic to create a function to Split the string on a " " (space) delimiter and join using a - hyphen.
#'for' will be used here
def manual_split_and_join(line):
     result=[]#an empty list
#look at every character of the provided string one by one
     for char in line:
          if char==" ":
               result.append("-") #if it is a space, replace it with hyphen instead
          else:
               result.append(char) #if it is any other character- no change 
     return "".join(result)               



#test the function
if __name__ == '__main__':
    line=input("enter the string:")
    print("original version:",split_and_join(line))   
    print("modified verion(removed unnecessary for loop):",split_and_join1(line))
    print("another modified version(manual version):",manual_split_and_join(line))