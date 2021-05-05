n = int(input('Enter a value: '))

print('Befor if condition')

if n>=0 :
    print('Positive Number')
    print('Value is:',n)
else:
    print('Negative number')
    print('Value is:',n)

print('After if condition')


#Nested if & elif statements

if n >= 0 :
    if n == 0:
        print('Zero number')
    else:
        print('positive number')
else:
    print('Negative number')

#Using elif function

if n > 0 :
    pritn('Positive Number')
elif n < 0 :
    print('Negative number')
else:
    print('zero Number')