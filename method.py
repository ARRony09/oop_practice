class Student:

    university='NSTU'

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    @classmethod
    def getUni(cls):
        return cls.university

    def info():
        print("This is Student class.. in abc module")

s1=Student(10,20,30)
s2=Student(20,20,40)
print(s1.avg())
print(s2.avg())
print(Student.getUni())
Student.info()