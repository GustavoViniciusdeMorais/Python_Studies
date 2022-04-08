import re
from abc import abstractmethod

'''
Python abc library is an Abstract Base Class
link to library https://docs.python.org/3/library/abc.html
'''

class Strategy():
    @abstractmethod
    def execute(self, a, b):
        pass

class ValidateStrategy(Strategy):
    def execute(self, a, b):
        a = str(a)
        b = str(b)
        reg = "^\d{1,2}"
        a = re.search(reg, a)
        b = re.search(reg, b)
        if a and b:
            return True
        else:
            return False

class AddStrategy(Strategy):
    def execute(self, a, b):
        a = int(a)
        b = int(b)
        return a + b

class SubStrategy(Strategy):
    def execute(self, a, b):
        a = int(a)
        b = int(b)
        return a - b

class Context():
    _strategy: Strategy

    def __init__(self, strategy: Strategy):
        self._strategy = strategy
    
    def set_strategy(self, strategy):
        self._strategy = strategy
    
    def execute(self, a, b):
        return self._strategy.execute(a, b)

class App():
    def example(self):
        a = input('a: ')
        b = input('b: ')
        validate = ValidateStrategy()
        context = Context(validate)
        valid = context.execute(a, b)
        
        if valid:
            add = AddStrategy()
            context.set_strategy(add)
            result = context.execute(a, b)
            print("Result is {}".format(result))
        else:
            print("The input must be only integer numbers")

app = App()
app.example()