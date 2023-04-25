class Animal:
    def __init__(self, name):
        self.myname = name

    def talk(self):
        raise NotImplemented("subclass must implement abstract method")


class Cat(Animal):
    def talk(self):
        return "Meow"


class Dog(Animal):
    def talk(self):
        return "Woof"


class Tiger(Animal):
    def talk(self):
        return "roar"

class Hyena(Animal):
    def talk(self):
        return "laughs"

class Lion(Animal):
    def talk(self):
        return "affirms"


simba = Lion("Virgil")
paka = Cat("Whiskers")
mbwa = Dog("Fido")
wild = Tiger("Russian")
fisi = Hyena("badboy")

print(simba.myname + " :" + simba.talk())
print(paka.myname + " :" + paka.talk())
print(mbwa.myname + " :" + mbwa.talk())
print(wild.myname + " :" + wild.talk())
print(fisi.myname + " :" + fisi.talk())
