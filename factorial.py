def fact_itr(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

def fact_rec(n):
    if n==0:
        return 1
    else:
        return n*fact_rec(n-1)

n=int(input("Please enter the number: \t\t"))
print("please enter you choice that how you want to calculate the factorial: \n\n")
m=int(input("1: Iteration       2:  Recursion \n\n"))
if m==1:
    f=fact_itr(n)
else:
    f=fact_rec(n)

print("Factorial of ",n," is ",f,"\n\n")