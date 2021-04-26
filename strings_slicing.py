# string[ starting_index : end_index : strike ]
my_str = 'Hello Python'

print(my_str[0:4])      #slicing will start from 0 and end before 4 and will not include the 4th element

print(my_str[6:9])      #output: Pyt will not include the 9th element

print(my_str[:8])       #slicing by default will start from 0 

print(my_str[3:])       #slicing will end at last index

print(my_str[0:8:2])    #strike start selecting every 2 element from starting

print(my_str[::-2])     #strike will start selecting every second element form last