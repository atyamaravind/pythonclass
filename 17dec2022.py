#polymorphism
"'jkhh'"
print(len("cipherschools"))
print(len([10,20,30,40]))

def sum(x,y,z=0):
    return x+y+z
print(sum(2,3))
print(sum(2,3,4))

class India:
    def capital(self):
        print("New Delhi")
def language():
    print("Multiple languages are spoken in words")
class Russia:
    def capital(self):
        print("Moscow")
def language(self):
    print("Russian")

obj9=India
obj0=Russia

print(id(obj9.capital))
print(id(obj0.capital))

class Bird():
    def intro(self):
        print("This is a bird class")

    def flight(self):
        print("Bird fly")

class Parrot(Bird):
    def flight(self):
        print("Parrot can fly")

class Ostrich(Bird):
    def flight(self):
        print("Ostrich can't fly")
obj1 = Bird()
obj2 = Parrot()
obj3 = Ostrich()

obj1.intro()
obj1.flight()

obj2.intro()
obj2.flight()

obj3.intro()
obj3.flight()
