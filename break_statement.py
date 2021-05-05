l = [10, 54 ,2 ,61, 14]

n = int(input('Enter search key:'))

for i in l:
    print(i,n)
    if i == n:
        print('found')
        break

#continue statement
l = [10, 54 , 2,  61, 15]

for i in l:
    if i % 2 != 0:
        continue
    print(i)