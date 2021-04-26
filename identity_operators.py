#Identity operators are (is , is not) and returns True if both operands point to the same reference in the memory
x = 10
y = 20

print( x is y)      #False
print( x is not y)  #True

#Membership Operator are (in , in not) and returns true if key id found in sequence.
S = 'Hello Python'

print('e' in S)     #True because e is present in s
print('p' in S)     #False because p is not present