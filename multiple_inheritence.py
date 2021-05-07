class A:
    def display(self):
        print('Method-A')

class B:
    def display(self):
        print('Mehtods-B')

class C(B,A):
    def displayC(self):
        print('Methods-C')


c = C()
c.display()
c.displayC()