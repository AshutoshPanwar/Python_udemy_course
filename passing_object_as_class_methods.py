class Students:
    def __init__(self,name,roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks
    def display(self):
        print('Students Name:',self.name)
        print('Roll Number:',self.roll)
        print('Marks',self.marks)
        
class Placements:
    def __init__(self,company,pakage,stud):
        self.company = company
        self.pakage = pakage
        self.stud = stud
    def display(self):
        self.stud.display()
        print('company Name:',self.company)
        print('Package:',self.pakage)

S = Students('Ashu',101,89.34)
#S.display()
P = Placements('dell', 48000, S)
P.display()