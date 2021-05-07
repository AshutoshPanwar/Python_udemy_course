class Students:
    def __init__(self,name,roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        print('Students Name:',self.name)
        print('Students roll no:',self.roll)
        print('Students marks:',self.marks)
        print()

S = Students('aaa',101,89.97)
S.display()
