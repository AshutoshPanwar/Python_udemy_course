class A:
    def displayA(self):
        print('Method-A')

class B:
    def displayB(self):
        print('Method-B')

class C(A):
    def displayC(self):
        print('Method-C')

class D(B,C):
    def displayD(self):
        print('Method-D')

d = D()
d.displayA()
d.displayB()
d.displayC()
d.displayD()