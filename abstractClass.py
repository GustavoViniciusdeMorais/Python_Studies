import sys

class Car(object):
    def run(self):
        pass
    def describe(self):
        pass

class Ferrari(Car):
    
    def __init__(self, mark, velocity):
        self.mark = mark
        self.velocity = velocity
    
    def run(self):
        return "Running at {} km".format(self.velocity)
    
    def describe(self):
        return "Ferrari of mark {} and speed of {}".format(self.mark,self.velocity)

f = Ferrari(sys.argv[1], sys.argv[2])
print(f.describe())
print(f.run())