class Students:
    '''this is version 1.0'''

    def __init__(self):
        self.name = 'Ashu'
        self.roll = 101
        self.marks = 80.93

    def __str__(self):
        return 'This is Studet class'

    def display(self):
        print('student name:',self.name)
        print('student roll number:',self.roll)
        print('marks:',self.marks)

S = Students()
print(S.name)
print(S.roll)
print(S.marks)
print(S.__doc__)
print(S)
S.display()


S1 = Students()
S2 = Students()
S3 = Students()
S1.display()
S2.display()
S3.display()
