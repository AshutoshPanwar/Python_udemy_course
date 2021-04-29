x = 10
y = 78.26

print('value of x is:',x)
print('value of y is:',y)

print('value of x is: %i' %x)       #here %i is used for integers
print('value of y is: %f' %y)       #here %f is used for float
print('value of y is: %i' %y)       #here observe that result is converted to integer
print('value of string is %s' %'Python')    #here %s is used for calling strings

print('Sum of %i + %i is %i' %(x,y,x+y))
print('Sum of %i + %f is %f' %(x,y,x+y))

print(y)
print(format(y,'.2f'))      #here .2f will round the number upto 2 decimal places