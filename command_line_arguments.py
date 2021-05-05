#only run this program through command line.

# command line arguments means passing the values through the command line interface
# To execute command line cariables we first write python3 and point towards the file

import sys

print(type(sys.argv))        #.argv stands for argument value <class-'lisy'>
print(len(sys.argv))

x = eval(sys.argv[1])
y = eval(sys.argv[2])

print(x+y)