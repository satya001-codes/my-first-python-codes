#program to wrap the given string into a paragraph of provided width
#input format:given a string and width
def text_wrap(string,max_width):
    chunks=[string[i:i+max_width] for i in range(0,len(string),max_width)] #stepis given to avoid repitition of the previous letter in the upcoming word
    return "\n".join(chunks) #to produce every word in a new line


#test the code
if __name__=="__main__":
    string=input("enter the string:")
    max_width=int(input("enter the width:"))
    result=text_wrap(string,max_width)
    print(result)