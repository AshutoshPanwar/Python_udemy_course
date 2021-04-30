#syntax of while loop
#while condition :
#     statement-1       (The statement is executed when the condition is true)

n = int(input('Enter value:'))

print('Number from 1 to ',n)

i = 1           #here i is the starting value of loop
while i <= n:
    print(i)
    i = i + 1

print('End of loop')