#range(start, stop, step)
# Range objects are immutable
#indexing and slicing can also be applied to range objects
#range function can 1, 2 ,3 parameters.

x = range(5)        #when the starting value is not given then range will starting from 0 to n-1

print(x)
print(x[0])         #indexing calling value at 0th place
print(x[4])         #indexing calling value at 4th place
#x[0] = 10           #Error because range is immutable

x = range(5,10)

print(x)

x = range(0,10,2)

print(x)

print(type(x))
