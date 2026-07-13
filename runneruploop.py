#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
#You are given n scores. Store them in a list and find the score of the runner-up.
n=int(input("enter n:")) #The first line contains n.[-100,100]
# The second line contains an array A[] of n integers each separated by a space.
arr=map(int, input("the individual's scores are:").split()) # The second line contains an array A[] of n integers each separated by a space.[-100,100]
highest=-101
runner_up=-101
for score in arr:
    if score>highest:
         runner_up=highest
         highest=score
    elif score>runner_up and score!=highest:
        runner_up=score
print("the runner_up score is:",runner_up)

