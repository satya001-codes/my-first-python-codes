#program to find the average score for the provided student's name if it exists in this database
n=int(input("enter the number of students:"))#The first line contains the integer , the number of students' records.
student_marks={}
# The next  lines contain the names and marks obtained by a student, each value separated by a space.
for _ in range(n):
    name, *line=input().split()
    scores=list(map(float, line))
    student_marks[name]=scores # The final line contains query_name, the name of a student to query.
# The final line contains query_name, the name of a student to query.
query_name=input("the name of the student whose average score is to be calculaated:")
if query_name in student_marks:
    query_scores=student_marks[query_name]
    avg_score=sum(query_scores)/len(query_scores)
    print(f"{avg_score:.2f}")
else:
    print("student",query_name,"does not exist in this database")
  