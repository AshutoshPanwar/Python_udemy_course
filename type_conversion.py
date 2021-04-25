# int type conversion.......
    print(2 + int(3.5))     #here int is a type casting function which will convert float into int but there is loss of data

    print(int(True))        #type casting can be applied to boolian also

    print(int('12'))        #string will convert to int it contain pure integers

    print(int('12.45'))     #float string can't be converted to int Error

# float type conversion .......
    print(2 + float(3))     #here 3 will be converted to 3.0 which is a float

    print(float(True))     #it will return 1.0

    print(flaot('12.45'))   #string will be coverted to float

    print(float('12'))      #Error int string can't be converted to float     


# bool type conversion........
    print(bool(2))          #every thing is true in bool weather it is float , int, str except 0

    print(bool(0))          #will always return 0

# str type conversion..........
    print(str(10))          #will convert int type into string

    print(str(10.75))       #will convert float into string

    print(str(True))        #even True which is boole will be printed as it is

    print(str(None))        #None will be printed

# complex type conversion...........
    print(complex(2))       #output: 2+0j (simple int is compared to real part)

    print(complex(2,3))     #output: 2+3j (first number is treated as real and second part as complex)

    print(complex(10.75))   #output: 10.75+0j 

    print(complex('3','6')) #Error we can not pass two strings

    print(complex('3+4j'))  #we can pass it as single string
    