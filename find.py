#program to count how many times a substring got repeated inside a string
def count_substring(string,sub_string):
    count=0
    #loop throug the string upto where can the string can totally fit
    for i in range(len(string)-len(sub_string)+1):
        if string[i:i+len(sub_string)]==sub_string: #slice through the string to match the substring length
            count+=1
    return count


#test the function
if __name__=="__main__":
    string=input("enter the string:")
    sub_string=input("enter the sub_string:")
    count=count_substring(string,sub_string)
    print(count)