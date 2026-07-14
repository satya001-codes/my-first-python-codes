#Given the names and grades for each student in a class of N students,store them in a nested list and print the name(s) of any student(s) having the second lowest grade
students=[] #an empty list
#input format- The first line contains an integer,N,the number of students.
#The 2N subsequent lines describe each student over 2 lines.
for _ in range(int(input())): #provided the input for the program
    name=input("enter the name:") #The first line contains a student's name.
    score=float(input("enter the scores:")) #The second line contains their grade.
    students.append([name,score])
scores=sorted(list(set([student[1] for student in students]))) #arrange the scores in ascending order
if len(scores)>1:
        second_lowestscore=scores[1]
        result_names=sorted([student[0] for student in students if student[1]==second_lowestscore]) # accessed the names for those scores
        for name in result_names:
                 print("the names of the students who got second lowest score:")
                 print(name)   
else:
       print("Not enough scores to compare!")
