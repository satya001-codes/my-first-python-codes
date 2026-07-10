#print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to n.
x=int(input("enter the value of x:"))
y=int(input("enter the value of y:"))
z=int(input("enter the value of z:"))
n=int(input("enter the value of n:"))
list=[] #i is is less than or equal to x, j is is less than or equal to y, k is less than or equal to z
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k!=n:
                list.append([i,j,k])
print(list)                