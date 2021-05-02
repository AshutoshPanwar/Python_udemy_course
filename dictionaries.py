#dictionaries have keys and values and are defined using curly brackets and each value pair is separated by collan
#instead of indexing we use keys
#keys are immutable and unique but dictionaries are mutable
#D = {'usa':100,'uk':200}       here usa-->key and 100-->value
D = {'USA':100,'UK':200,'india':300}
print(len(D))
#adding a new value to dictionary
D['Australia']= 400
print(D)
#deleting a value from the dictionary
del(D['UK'])
print(D)
#to see all the keys in dictionary
print(D.keys())
#to see all the values in dictionaryes
print(D.values())
#searching value in dictionaries
print('india' in D)

for i in D:
    print(i,D[i])