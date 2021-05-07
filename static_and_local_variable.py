class Students:
    def __init__( self,name,roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        print('Student Name',self.name)
        print('Students Roll No',self.roll)
        print('Students Marks:',self.marks)
        college = 'UCLA'
        print('college Name:',Students.college)
        print()

Students.college = 'UTD'
S1 = Students('aaa',101,89.12)
S2 = Students("bbb",102,55.63)
S1.display()
S2.display()