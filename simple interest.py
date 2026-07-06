p = float(input("money lent:"))  #p is principal amount 
r = float(input("rate% (per annum):")) 
t = float(input("time(in years):"))
s = (p*r*t)/100  #s is simple interest
a = s+p  #a is amount payable
print("simple interest =",s)
print("amount payable =",a)