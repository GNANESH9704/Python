def staircase(n):
    if n==1:
        return 1
    if n==2:
        return 2
    else:
        return staircase(n-1)+staircase(n-2)
n=int(input("enter the number of steps in staircase= "))
print("number of ways to climb the staircase= ",staircase(n))
