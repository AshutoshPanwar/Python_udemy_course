t = (10,30,20,60)
print(t)
print(type(t))
print(len(t))


t1 = (10,'hello',2.32)
print(t)
print(type(t))
print(len(t))

print(t[0])
print(t[2])
print(t[-1])

t2 = t1 + (5.42,'python')
print(t2)

#we can not del(t[1]) because tuples are immutable