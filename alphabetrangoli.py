#program to print alphabet rangoli
def print_rangoli(size):
    import string
    alpha=string.ascii_lowercase
    lines=[]
    for i in range(size):
        s="-".join(alpha[i:size])
        row=s[::-1]+s[1:]
        lines.append(row.center(4*size-3,"-"))
    print("\n".join(lines[::-1]+lines[1:])) 


#test the code
if __name__=="__main__":
    n=int(input("enter the size that u want the rangoli to have:"))
    print_rangoli(n)       
