#Given an integer,n, and n space-separated integers as input, create a tuple,t, of those n integers. Then compute and print the result of hash(t).
n=int(input("the no of elements in the tuple is:"))#The first line contains an integer,n, denoting the number of elements in the tuple.
integer_list=map(int,input("provide the elements:").split())#The second line contains n space-separated integers describing the elements in tuple t.
t=tuple(integer_list)
print("the hash value of the provided tuple is:",hash(t))
