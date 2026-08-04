#program to design a doormat in a specific way
#input:N must be an odd natural number and M should be three times N
N, M=map(int,input().split()) 
#or,text=input().split()   N=int(text[0])   M=int(text[1])
for i in range(1,N,2):
    pattern=".|."*i
    print(pattern.center(M,"-"))
print("WELCOME".center(M,"-"))
for i in range(N-2,-1,-2):
    pattern=".|."*i
    print(pattern.center(M,"-"))

