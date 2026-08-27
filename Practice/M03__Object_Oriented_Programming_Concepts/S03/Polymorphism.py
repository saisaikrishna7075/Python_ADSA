class Animal:
    def sound(self):
        print("Animal makes Sound")
class Dog(Animal):
    def sound(self):
        print("Bow-Bow")
class Cat(Animal):
    def sound(self):
        print("Meow-Meow")
        super().sound()
