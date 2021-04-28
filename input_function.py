x = input('Enter a value of x:')
y = input('Enter a value of y:')

print(float(x) + float(y))
print(int(x) + int(y))
print(eval(x) + eval(y))    #Best practice
print(type(x + y))      #class:'str'

#Reading multiple Values
w,z = input('Enter the values: ').split()     #Enter the 10 20
print(z)
print(w)
