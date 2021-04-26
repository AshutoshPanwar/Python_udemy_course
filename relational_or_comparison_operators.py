# relational operators are (<, <= , >, >=) and always return a boolean value
    x = 10
    y = 20 
    print(x <= y)       #True

    x = 'hello'
    y = 'python'
    print(x > y)        #False

#chaining of relational operators
    w,x,y,z = 10,20,30,40

    print(w < x < y < z)    #True
    print(w < x > y < z)    #False

#Equality operators are Equal to(==), Not Equal to(!=)
    x = 10
    y = 10.0
    z = True

    print(x == y)       #True
    print(x != y)       #False
    print(1 == z)       #True
