#with same data type
l = [10, 20 , 30 ,35, 68]
print(l)
print(type(l))
print(len(l))

#with mixed data type
l = [10, 'hello', 3.45]
print(l)
print(type(l))
print(len(l))
print(l[1])
print(l[0])
print(l[-1])

#lists are mutable
print(l)
l[1] = 'python'
print(l)