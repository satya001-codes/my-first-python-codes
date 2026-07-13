#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
#You are given n scores. Store them in a list and find the score of the runner-up.
n=int(input("enter n:")) #The first line contains n.
# every value written after space is treated as individual score.
arr=map(int, input("the scores are:").split()) # The second line contains an array A[] of n integers each separated by a space.
unique_scores=set(arr) #removes duplicates
sorted_scores=sorted(unique_scores) #arrange the values in ascending order
runner_up=sorted_scores[-2]
print("the runner up score is:",runner_up)



