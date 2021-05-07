class A:
    def display(self):
        print('class A method')

class B:
    def display(self):
        print('class B method')

class Demo(B,A):
    def display(self):
        print('class Demo method')


d = Demo()
d.display()
print(Demo.mro())