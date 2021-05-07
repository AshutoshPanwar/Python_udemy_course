class students:

    def setName(self,n):
        self.__name = n
    def getName(self):
        return self.__name

    def setMarks(self,m):
        self.__marks = m
    def getMarks(self):
        return self.__marks

    def  display(self):
        print('Name:',self.getName())
        print('Marks:',self.getMarks())

S = students()
S.setName('Ashu')
S.setMarks(98.87)
S.display()