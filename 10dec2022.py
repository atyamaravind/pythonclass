#inheritance
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
            print(self.name, self.age)


class Employees(Person):
    pass
a=Employees("Anurag","20")
a.display()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name, self.age)
class Employee(Person):
    def __init__(self, name, age):
        Person.__init__(self, name, age)
a = Employee("Anurag","20")
a.display()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name, self.age)
class Employee(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
a = Employee("Anurag","20")
a.display()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Employee(Person):                 '''(paramatarized funtion)'''
    def __init__(self, name, age, year):
        super().__init__(name, age)
        self.year = year

    def welcome(self):
        print("Hi welcome ",self.name, "whose age is",self.age,"to the year", self.year)
a = Employee("Anurag",20,2022)
a.welcome()
