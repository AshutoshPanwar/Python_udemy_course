#list are an ordered sequence of data which are created by using elents separated by commas within square brackets
#list are immtable and can have mixed data type.

L1 = [10, 'hello', 2.85]
#we can call number using indexing
print(L1[0])
print(L1[1])
print(L1[2])
#we can add two lists using + operator
L2 = L1 + [56.5,'python']
print(L2)
#we can also insert elements using .insert() or append() or extend()
L1.insert(1,20)     #20 will be inserted at 1 index
print(L1)
L1.append(56.5)
print(L1)
L1.extend([56.5,'python'])
print(L1)
#we can also delete elements
del(L1[1])
print(L1)
print(L1[0:4])

my_str = "Hello Python"
print(my_str.split( ))

L = [10 ,54 , 2, 61 , 13]
L.sort()
print(L)

L.reverse()
print(L)

print(len(L))

print(sum(L))

print(min(L))

print(max(L))

print(54 in L)