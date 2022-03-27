class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eatdrink(self):
        print("Eat Biryani and Drnk Beer")


class Employee(Person):
    def __init__(self,name,age,eno,esal):
     super().__init__(name,age)
     self.eno = eno
     self.esal = esal

    def work(self):
        print("coding is easy when you do more parctice")
    def empinfo(self):
        print("Employee Name:",self.name)
        print(" Employee Age:",self.age)
        print("Employee Number:",self.eno)
        print("Employee Salary:",self.esal)

e = Employee('raju',48,555,3454)
e.eatdrink()
e.work()
e.empinfo()

class Car:
    def __init__(self,name,model,color):
        self.name = name
        self.model = model
        self.color = color
    def getinfo(self):
        print("\tCar Name:{}\n\t Model:{}\n\t Color:{}".format(self.name,self.model,self.color))

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eatdrink(self):
        print("Eat Biryani and Drink Beer")

class Employee(Person):
    def __init__(self,name,age,eno,esal,car):
        super().__init__(name,age)
        self.eno = eno
        self.esal = esal
        self.car = car
    def work(self):
        print("coding python is very esay ")
    def empinfo(self):
        print("Employee Name:",self.name)
        print("Employee Age:",self.age)
        print("Employee number:",self.eno)
        print("Employee car info:")
        self.car.getinfo()


c = Car("Innvoa","2.5V","Gray")
e = Employee("Durga",48,100,1000)
e.eatdrink()
e.work()
e.empinfo()

class Student:
    collegeName = 'DURgasoft'
    def __init__(self,name):
        self.name = name
print(Student.collegeName)
s = Student('durga')
print(s.name)


class P:
    def __init__(self):
        print(id(self))

class C(P):
    pass
c = C()
print(id(c))


