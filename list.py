#lists are mutable
#Lists are an ordered sequence of data, separated by commas within square brackets.
#lists are mutable and can have int, str, float as values.
#Elements of list can be accessed by using indexing start from 0 and opposite with -1.
l1 = [10, 'hello', 2.85]
print(l1[0])        #index 0 stands for 1 value
print(l1[1])        #index 1 srands for 2 value
print(l1[2])        #index 2 stands for 3 value

#Adding two lists
l2 = l1 + [56.4, 'python']
print(l2)

#insert elements
l = [10 , 20 ,30]
print(l.insert(1, 22))
print(l.extend([55.4, 'python']))      #.extend only takes lists
l1[1] = "added"