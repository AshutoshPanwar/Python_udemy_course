class Demo:

    @staticmethod
    def add(x,y):
        print('Sum:',x+y)

    @classmethod
    def add(cls,x,y):
        print('Sum:',x+y)

D = Demo()
D.add(10,20)
#or
Demo.add(10,20)