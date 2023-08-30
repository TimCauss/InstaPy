

class Person:

    species = 'Homo Sapiens'
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1

    def display(self):
        print(f'{self.name} is {self.age} years old')


p1 = Person('John', 20)
p2 = Person('Jack', 34)

p1.display()
p2.display()
