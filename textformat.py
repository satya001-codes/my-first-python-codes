#program to print the following values for each integer i from 1 to n(given:integer n):decimal,octal,hexadecimal(capitalized) and binary
def print_formatted(number):
#Each value should be space-padded to match the width of the binary value of number and the values should be separated by a single space.    
    width=len(bin(number)[2:])
    for i in range(1,n+1):
        dec=str(i)
        octal=oct(i)[2:]
        hexa=hex(i)[2:].upper()
        binary=bin(i)[2:]
        print(f"{dec.rjust(width)} {octal.rjust(width)} {hexa.rjust(width)} {binary.rjust(width)}")


#test the code
if __name__=="__main__":
    n=int(input())
    print_formatted(n)        