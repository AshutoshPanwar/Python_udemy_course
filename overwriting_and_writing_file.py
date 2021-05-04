#To over write the content of a file
FileWrite = open('writing.txt','w')

FileWrite.write('new line-1\n')
FileWrite.write('new line-2\n')
FileWrite.write('new line-3\n')

FileWrite.close()

# to write text without remocing the existing content
fileWrite = open('writing.txt','a')

L = [55,65,75]
for i in L:
    fileWrite.write(str(i)+'\n')