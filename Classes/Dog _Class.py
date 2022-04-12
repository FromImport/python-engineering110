class Dog:
    animal_kind = "canine"

    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
        self.bark()

    def bark(self):
        return "woof"

fido = Dog("Lucky", "Brown")

print(fido.name)
print(fido.colour)
print(fido.bark())
