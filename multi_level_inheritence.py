class A:
    def __init__(self):
        print('Consturctour-A')
    def displayA(selfl):
        print('Method-A')

class B(A):
    def __init__(self):
        print('Constructor-B')
    def displayB(self):
        print('Method-B')

class C(B):
    def __init__(self):
        print('Constructor-C')
    def displayC(self):
        print('Method-C')

c = C()
c.displayB()
c.displayA()
c.displayC()