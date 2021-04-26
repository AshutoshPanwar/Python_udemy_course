#in total there are 7 arithmetic operators in python
print(3 + 4)    #adding two integers will give ans in integer
print(2.5 * 2)  #operation between float or int will always give us float numbers
print(2 - 15)   #ans would be an integer

#Division(/) operator result is always float..
print(10 / 2)   #output: 5.0 which is float
print(5 / 0)    #Error second number can not be 0
#Modulus(%) operator will returns the remainder in integer or float value
print(14 % 4)   #3*4+2 = 2 remainder
print(14.75 % 4)#3*4+2.75 = 2.75 remainde
print(5 / 0)    #Error 0 division error
#Exponential(**) operator become power of the number
print(2 ** 3)   #2*2*2 = 8
print(3.5 ** 2) #3.5*3.5 = 12.25

#Addition(+) operator can also be applied on strings 
print(2 + 3)    #will get 5 as ans because + operator will add both operants
print('hello'+'python')#will print hellophthon because + operator will add both strings

#Multiplication(*) operator can also be applied on strings
print('hello' * 3)  #will print hello three times as hellohellohello
print(True * 'hello')   #will print hello because True boolen has value as 1
print(False * 'hello')  #will print nothing because False has value 0

#Arthmetic operator on conplex numbers (//,% are not possible)
z1 = 2 + 3j
z2 = 4 - 6j

print(z1 + z2)  
print(z1 * z2)
print(z1 / z2)
print(z1 % z2)
print(z1 ** z2)