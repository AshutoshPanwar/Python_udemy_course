# we have print() as an output statement
#observe the difference

print('Hello')
print('Hello\nPython')
print('Hello\tPython')
print('Hello'+'Python')
print('Hello'*5)

x = 10
y = 20
z = 30
print('values are:',x,y,z)        #sunce we have used , to seperate the result will be seperated by space
print(x+y+z) 

x = '10'
y = '20'
z = '30'
print(x,y,z)        #sunce we have used , to seperate the result will be seperated by space
print(x+y+z)        #Observe the difference 

x,y,z = 10,20,30

print(x,y,z,sep=':')
print(x,y,z,sep='<--')

print(x,end='-')
print(y)