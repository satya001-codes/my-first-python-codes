name=input("enter the name:")
y=int(input("enter year of birth:"))
c=int(input("enter current year:"))
a=c-y #age of the person
if a<=100:
    p=(100-a)+c #when the person will turn 100
    print("the person's 100th birthday will be celebrated in the year",p)
else:
    print("the person had already celebrated his/her 100th birthday")
