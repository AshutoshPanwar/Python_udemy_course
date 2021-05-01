#Tuples are an ordered sequence of data which are created using elements seperataed by commas within parenthesis.
#Tuples are immutable and can have mixed data type

tup = (10, 'hello',2.85)
#to access the elements of tuple we use indexing
print(tup[0])
print(tup[1])
print(tup[-1])
#we can add tuples by using + operator
tup2 = tup + (4.52,'python')
print(tup2)
#we can also do slicing in tuples
print(tup2[0:3])
#to find the lenglt of tuple we use .len() method
print(len(tup))
#we can also find the sum of typle using the sum()
tup3 = (13,32,54,23,11)
print(sum(tup3))
#we can also find the minimum value in tuple
print(min(tup3))
#we can also find the maximum value in tuple
print(max(tup3))
#we can search an element using in function
print(54 in tup3)