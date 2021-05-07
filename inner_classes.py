class College:
    def __init__(self):
        print('Outer Class Constructor')

    class Student:
        def __init__(self):
            print('Inner Class constructor')
        def displayS(self):
            print('Students Method')

    def displayC(self):
        print('College Method')

C = College()
C.displayC()
# S = C.Student()
# S.displayS()
s = College().Student()
s.displayS()