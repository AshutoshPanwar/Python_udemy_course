#Bitwise operaors are (&, |, ^ , ~ , << , >>) and only works on integers and boolean
#Integers are ocverted into binary numbers and binary numbers are represented as 32 bits
print(9 & 12)       #output: 8 (the numbers are first converted to binary numbers)
print(bin(9))       #binary representation of 9
print(bin(12))      #binary representation of 12
print(bin(8))       #binary representation of 8

print(9 | 12)       #output: 13 (the numbers are first converted to binary numbers)
print(bin(9))       #binary representation of 9
print(bin(12))      #binary representation of 12
print(bin(13))      #binary representation of 13

#we can apply same for boolian values
print(True & False)      
print(True | False)

#Assignment opperators( += , -= , *= , /= , %= , //=, **=)
x = 10
x += 2
print(x)            #output: 12 (x = x+2)
x *= 2
print(x)            #output: 20 (x = x*2)
