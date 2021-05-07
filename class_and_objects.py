
class Students:
    '''this is version 1.0'''
    def __init__(self,name,roll,marks):
          self.name = name
          self.roll = roll
          self.marks = marks

    def __str__(self):
        return 'This is Studet class'

    def display(self):
        print('student name:',self.name)
        print('student roll number:',self.roll)
        print('marks:',self.marks)

S1 = Students('aaa', 101, 83.24)
S2 = Students('bbb', 102, 24.56)
S3 = Students('ccc', 103, 63.53)
#or

S = [Students('aaa', 101, 83.24),
     Students('bbb', 102, 24.56),
     Students('ccc', 103, 63.53)]

S1.display()
S2.display()
S3.display()

for i in S:
    i.display()
