#sets are also type of collection and are unordered ie do not have any position
#sets have only unique elements

#we can convert a list into set using set()
L = [10,'hello', 2.34, 10 ,'python']
S = set(L)
print(S)

#we can also add elements using .add()
S.add('Australia')
print(S)
#we can also remove element using .remove method
S.remove(10)
print(S)
#to know the number of elements in set we use len()
print(len(S))
#to check weather a element is a member of set we use in 
print('hello' in S)

#we can also apply mathematical operations on sets like
S1 = {'usa','uk','india','australia'}
S2 = {'australia','usa','canada'}

S3 = S1 & S2
print(S3)
S4 = S1.union(S2)
print(S4)

D = {10,20,30,40}
for i in D: 
    print(i)