l = [20, 'hello' ,2.45]

#.insert is used to insert element at perticular index
l.insert(1, 690)
print(l)

#.extend is used to insert more than one elements and take only list as arguments
l.extend([4.34, 50])
print(l)

del(l[1])
print(l)