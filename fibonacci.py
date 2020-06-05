#this program is wrong
def fib(n):
    if(n==0 or n==1):
        return n
    else:
        return fib(n-1)+fib(n-2)

n=int(input("Please enter the last number\n"))
f=fib(n)
print(fib(n))