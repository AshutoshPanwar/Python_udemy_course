#Lambda functions are known as the name less functions
#Lambda functions are created for one time use or for instant use

#Let's first diclare a simple function to understand the lanbda function
def myfunction(n):
    return n*n

result = myfunction(4)
print(result)

#now making a lanbda function
res = lambda n: n*n
print(res(3))