"""class Bank_account:
    def set_details(self,name,balance=0):
        self.name=name
        self.balance=balance
    def display(self):
        print(f"{self.name} and balance is {self.balance}")
    def withdraw(self,amount):
        self.balance=self.balance-amount
    def deposit(self,amount):
        self.balance=self.balance+amount

B=Bank_account()
B.set_details("Rony",100)
B.display()
B.withdraw(50)
B.display()
"""

"""
class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage

a=Vehicle(120,18)
print(a.max_speed)
print(a.mileage)"""

"""class Vehicle:
    def __init__(self):
        pass"""

"""class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

a=Bus("Bmw",120,18)
print(f"Vehicle Name:{a.name} Speed: {a.max_speed} mileage: {a.mileage}")"""
"""
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


a=Bus("Bmw",150,20)
print(a.seating_capacity())"""
"""
class Vehicle:
    color="White"
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def show(self):
        return f"Color:{self.color} Vehicle name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}"
class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass


a=Vehicle('BMW',150,20)
print(a.show())"""


"""class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        return self.capacity*100+self.capacity*100*0.1

a=Bus('School volvo',12,50)
print('Total Bus fare is:',a.fare())"""

"""class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

a=Bus("School Volvo", 12, 50)
print(a)"""

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)

print(isinstance(School_bus,Vehicle))