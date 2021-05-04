FileRead = open('data.txt','r')

contents = FileRead.read()
print(contents)

content = FileRead.readlines()
print(content)

for line in content:
    print(line)