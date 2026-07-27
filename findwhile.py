#a program to count how many times a substring got repeated inside a string using find
def count_substring_find(string,sub_string):
    count=0
    start=0 #it tells python the index from where to begin searching inside the string
    while True: #while is used because i don't know how many steps it will take 
        pos=string.find(sub_string,start) #'pos' returns the index where it find a match after looking from the index given in the start
        if pos!=-1: #pos return -1 when it didn't find a match
            count+=1 
            start=pos+1  #starts looking after the index where it previously found a match
        else:
            break  #without it, output is not produced because while loop runs infinitely
    return count        
            


#test the output
if __name__=="__main__":
    string=input("enter the string:")
    sub_string=input("enter the sub_string:")
    loop=count_substring_find(string,sub_string)
    print(loop)


