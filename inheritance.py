class Person:
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber

    def display(self):
        print(f"My name is {self.name} and id number is {self.idnumber}")

class Employee(Person):
    def __init__(self, name, idnumber,post,salary):
        super().__init__(name, idnumber)
        self.salary=salary
        self.post=post
        
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
        print("Post: {}".format(self.post))

a=Employee('Rony',198219,"Intern",10000)
a.display()
a.details()