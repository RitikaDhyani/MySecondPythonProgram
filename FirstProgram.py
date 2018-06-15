print("To check no. of 1's")
num=int(input(" Total numbers"))
x=0
count=0
while x<num:
    n=int(input("Enter the number"))
    if n==1:
        count=count+1
    x=x+1
print("The no. of 1's",count)