#a function to Split the string on a " " (space) delimiter and join using a - hyphen.
def split_and_join(line):
    for char in line:
        a=line.split()
    return "-".join(a) 

#test the function
if __name__ == '__main__':
    line=input("enter the string:")
    result=split_and_join(line)
    print(result)   