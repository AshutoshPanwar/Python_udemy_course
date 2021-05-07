class Students:
    def __init__(self,name,roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        print("Students Name",self.name)
        print("Students Roll no:",self.roll)
        print("student Marks:",self.marks)
        print()

    def profile(self):
        self.city = 'London'
        States = 'ABC'
S = Students('aaa', 101, 98.23)
print(S.__dict__)
S.marks = 54.73
print(S.__dict__)
S.grade = 'A'
print(S.__dict__)
S.profile()
print(S.__dict__)
del S.marks
print(s.__dict__)