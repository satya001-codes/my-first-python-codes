#another shortcut way
#program to print the following values for each integer i from 1 to n(given:integer n):decimal,octal,hexadecimal(capitalized) and binary
def print_formatted1(number):
#Each value should be space-padded to match the width of the binary value of number and the values should be separated by a single space.    
    width=len(bin(number)[2:])
    for i in range(1,n+1):
#d=decimal o=octal X=capital hexadecimal  b=binary
#{i:{width}d} python right aligns numbers when padded this way and they automatically remove the Oo,Ox and Ob prefix.        
        print(f"{i:{width}d} {i:{width}o} {i:{width}X} {i:{width}b}")


#test the output
if __name__=="__main__":
    n=int(input())
    print_formatted1(n) 