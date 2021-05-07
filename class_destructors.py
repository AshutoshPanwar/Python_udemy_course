class Demo:
    def __init__(self):
        print('constructor called')

    def display(self):
        print('Display Method called')

    def __del__(self):
        print('Destructor called')

D = Demo()
D.display()