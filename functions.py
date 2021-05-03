# Function is block or a piece of code which only runs only when it is called.
#All function starts form def.
def display():
     print('Hello')
     print('Python')

def mysum(a,b):
    c = a + b
    return c

def mymul(a,b):
    c = a * b
    return c
    
display()       #calling the function
display()       #we can a function n number of times

x = mysum(10,23)
print(x)
y = mymul(32,24)
print(y)
y = mymul('Python',4)
print(y)

#keyword argument
def myfunction(x,y,z):
    print('value X:',x)
    print('value y:',y)
    print('value z:',z)
    w = x+y+z
    print('value of w:',w)

myfunction(z=3,x=5,y=8)
myfunction(3,z=5,y=8)

#User defined function (we can provide the default values to the function)
def myfunction(x,y=4,z=7):
    print('value X:',x)
    print('value y:',y)
    print('value z:',z)
    w = x+y+z
    print('value of w:',w)

myfunction(10)
myfunction(10,8)

