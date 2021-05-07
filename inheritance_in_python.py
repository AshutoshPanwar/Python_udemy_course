class Students:
    def __init__(self):
        self.name = ''
        self.roll = 0
        self.marks = 0
    def getStudentsData(self,name,roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks
    def displayS(self):
        print(self.name,self.roll,self.marks)

class Placements(Students):
    def __init__(self):
        self.company = ''
        self.package = ''
    def getPlacementData(self,company,package):
        self.company = company
        self.package = package
    def displayP(self):
        print(self.company,self.package)

P = Placements()
P.getStudentsData('Ashu', 101, 90.45)
P.getPlacementData('Dell', 48000)
P.displayS()
P.displayP()