class A:
    def displayA(self):
        print('Method-A')

class B(A):
    def displayB(self):
        print('Method-B')

class C(A):
    def displayC(self):
        print('Method-C')

c = C()
c.displayA()
c.displayC()