#program to generate a symbol for hackerrank in  a particular way
#the thickness must be an odd number
thickness=int(input("enter the thickness:"))
c='H'
#the top cone
for i in range(thickness+1):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
#the pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
#the mid partition
for i in range((thickness+1)//2):
    print((c*(thickness*5)).center(thickness*6))
#the pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
#the bottom cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))                