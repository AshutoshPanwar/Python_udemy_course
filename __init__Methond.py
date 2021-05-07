class Students:
    def __init__(self):
        self.name = 'abc'
        self.roll = 101
        self.marks = 78.23
        print('In Constructor')

    def display(self):
        print(self.name,self.roll,self.marks)

s = Students()
s.__init__()