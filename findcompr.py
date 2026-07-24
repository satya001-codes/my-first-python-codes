#program to count how many times a substring got repeated inside a string using list comprehension
def count_substring_comprehension(string,sub_string):
    #generates 1 for every match and sums them up
    return sum(1 for i in range(len(string)-len(sub_string)+1) if string[i:i+len(sub_string)]==sub_string)


#test the code
if __name__=="__main__":
    string=input("enter the string:")
    sub_string=input("enter the sub_string:")
    count=count_substring_comprehension(string,sub_string)
    print(count)