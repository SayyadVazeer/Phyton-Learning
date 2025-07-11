

class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True
    
    def eat(self):
        print(f"{self.name} can eat")
    
    def sleep(self):
        print(f"{self.name} can sleep")

class Dog(Animal):
    def bark(self):
        print("Bow Bow Bow !")
        super().eat()

class Cat(Animal):
    def __init__ (self, name , magic):
        super().__init__ (name)
        self.magic = magic
    def mag(self):
        print(f" {self.name} can do {self.magic} magic")
class Mouse(Animal):
    pass

class walk(Dog):
    pass
dog = Dog("Scooby")
cat = Cat("Garfield", " Black ")
mouse = Mouse("Micjey")

pink = walk("Bannu")

pink.bark()
cat.mag()