class Student:
    def __init__(self,name,rollno,marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks
    def talk(self):
        print("my name is:",self.name)
        print("my rollno is:",self.rollno)
        print("my marks are:",self.marks)

s1 = Student("Raju",102,35)
s1.talk()

class Employee:
    def __init__(self,empname,empage,empsal,empaddrs):
        self.emapname = empname
        self.empage = empage
        self.empsal = empsal
        self.empaddrs = empaddrs

    def talks(self):
        print("Employee name is:",self.emapname)
        print("Employee age is:",self.empage)
        print("Employee salary is:",self.empsal)
        print("Employee Address is :",self.empaddrs)

E1 = Employee("Ritesh",23,50000,"Kalamboli")
E1.talks()

E2 = Employee("Ganga",24,60000,"Pune")
E2.talks()

E3 = Employee("Raju",35,200,"Nanded")
E3.talks()

class Student:
    def __init__(self,name,rollno,marks):
        print('''creating instance variable and initialization''')
        self.name = name
        self.rollno = rollno
        self.marks = marks
s2 = Student("raju",20,32)
print(s2.name,s2.rollno,s2.marks)
s3 = Student("raju",22,33)
print(s3.name,s3.rollno,s3.marks)
s4 = Student("raju1",23,34)
print(s4.name,s4.rollno,s4.marks)


class Test:
    def __init__(self):
        print("Constructor Execution")

t = Test()
t.__init__()
t.__init__()
t.__init__()
t.__init__()
