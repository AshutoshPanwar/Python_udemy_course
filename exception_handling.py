#various errors may occure at runtime and when this occure the program terminates

l = [10,20,30,40]

try:
    print(l[10])
except IndexError as e:
    print(e)
# Or
try:
    print(l[30])
except Exception as e:
    print(e)
    
print(l)