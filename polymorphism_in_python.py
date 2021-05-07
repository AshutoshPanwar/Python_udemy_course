class A:
    def display(self):
        print('Value',0)

class B(A):
    def display(self):
        print('Value:',1)


b =  B()
b.display()