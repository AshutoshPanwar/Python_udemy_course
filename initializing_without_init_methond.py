class Student:
    def init(self,name,roll,marks):
        self.name = name
        self.roll = roll
        self.marks =  marks

    def display(self):
        print('Student Name:',self.name)
        print('Roll Number:',self.roll)
        print('Marks:',self.marks)

S = Student()
S.init('Ashu', 101, 89.24)
S.display()