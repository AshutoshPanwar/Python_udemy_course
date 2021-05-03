#recursion means making a function that can call it self.

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact

num = input("Enter Number:")
num = int(num)
print(factorial(num))

def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)

num = input("Enter Number:")
num = int(num)
print(factorial(num))