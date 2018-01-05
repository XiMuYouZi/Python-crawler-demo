class Xiaorui:
    def __init__(self):
        self.name = 'fengyun'

        def setName(self, name):
            self.name = name

        def getName(self):
            return self.name

        def greet(self):
            print('Hello, i’m % s' % self.name)


foo = Xiaorui()
print(getattr(Xiaorui, 'greet', 'not found'))
print(getattr(foo, 'age', 'not foun'))
