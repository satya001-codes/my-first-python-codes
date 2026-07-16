#program to give the command to an list and then perform it accordingly
n=int(input("enter the number of commands:")) #The first line contains an integer,n, denoting the number of commands.
#Each line i of the n subsequent lines contains the commands.
list=[] #creating an empty list
for _ in range(n):
    parts=input().split()
    command=parts[0]
    if command == "insert": #insert i e: Insert integer e at position i
        position=int(parts[1])
        value=int(parts[2])
        list.insert(position,value)
    elif command=="print":  #print the list
        print(list)
    elif command=="remove": #remove e: Delete the first occurrence of integer e.
        value=int(parts[1])
        list.remove(value)
    elif command=="append": #append e: Insert integer e at the end of the list.
        value=int(parts[1])
        list.append(value)
    elif command=="sort": #sort the list.
        list.sort()
    elif command=="pop": #pop the last element from the list.
        list.pop()
    elif command=="reverse": #reverse the list.
        list.reverse()
    else:
        print("the given command is not operatable in this database!")

                 