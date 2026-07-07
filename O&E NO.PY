#it will display weird if n is odd or n is even and in the inclusive range of 6 and 20
#it will display weird not weird in all other cases

n=int(input("enter the number:"))
if n%2==0:
    if n<=5 and n>=2:
        print("Not Weird")
    elif n>=6 and n<=20:
        print("Weird")
    else:
        print("Not Weird") 
else:
    print("Weird")    
