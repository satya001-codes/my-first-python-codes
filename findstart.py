#program to find a substring inside a string using startswith function
def count_substring_startswith(string,sub_string):
    count=0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count+=1
    return count        


#test the output
if __name__=="__main__":
    string=input("enter the string:")
    sub_string=input("enter the sub_string:")
    count=count_substring_startswith(string,sub_string)
    print(count)