"""class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    
    def perimeter(self):
        return 2*(self.length+self.width)
    
    def area(self):
        return self.length*self.width
    
    def display(self):
        return f"Length: {self.length} Width:{self.width} Perimeter:{self.perimeter()} Area:{self.area()}"


class Parallelepipede(Rectangle):
    def __init__(self, length, width,height):
        super().__init__(length, width)
        self.height=height
    
    
    def volume(self):
        return f"Volume: {self.length*self.width*self.height}"

a=Rectangle(10,5)
b=Parallelepipede(10,5,3)
print(a.display())
print(b.volume())"""

"""
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        return f"Name:{self.name} and age:{self.age}"


class Student(Person):
    def __init__(self, name, age,section):
        super().__init__(name, age)
        self.section=section

    def displayStudent(self):
        return f"Name:{self.name} and age:{self.age} and section: {self.section}"

a=Student('Rony',20,"Padma")
print(a.displayStudent())"""


