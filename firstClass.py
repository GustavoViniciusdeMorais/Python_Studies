class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def describe(self):
        return "My name is {}, and i'm {} years old".format(self.name, self.age)

gustavo = Person('Gustavo', 25)
print(gustavo.describe())