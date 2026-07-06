#program to tell the user the year in which he/she will turn 100 years old
name=input("enter your name:")
age=int(input("enter your age in the current year:"))
c=int(input("the current year:"))
if age<=100:
        y=c+(100-age)
        print(name,"will celebrate his/her 100th birthday in",y)
else:
        print("congratulations!",name,"has aleady celebrated his/her 100th birthday.")
