"/ Uzd1 /"
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def info(self):
        print(f"Person: name = {self.name} ; age = {self.age} ")

myObj = Person("John", 23)
myObj.info()

"/ Uzd2 /"

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Person: name = {self.name} ; age = {self.age}"

myObj = Person("John", 23)
print(myObj)

"/ Uzd3 /"

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,value):
        if value < 0:
            print("Число не должно быть меньше нуля!")
            self.__age = 0
        else:
            self.__age = value

    def __str__(self):
        return f"Person: name = {self.name} ; age = {self.__age}"

myObj = Person("John", -1)
print(myObj)

"/ Uzd4 /"

class Employee:
    name = None
    __salary = None

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    
    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self,money):
        if money < 0:
            print("Зарплата не может быть отрицательной!")
            self.__salary = 0
        else:
            self.__salary = money
    
    def increase_salary(self, percent):
        if percent > 0:
            x = percent / 100
            res1 = self.salary * x
            res2 = self.salary + res1
            res2 = int(res2)
            self.__salary = res2
        if percent <= 0:
            pass
        
    def __str__(self):
        return f"Employee: name = {self.name}, salary = {self.__salary}"

emp = Employee("Anna", -500)
print(emp)

emp.salary = 1000
emp.increase_salary(20)
print(emp)

"/ Uzd5 /"

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,value):
        if value < 0:
            print("Число не должно быть меньше нуля!")
            self.__age = 0
        else:
            self.__age = value

class Student(Person):
    def __init__(self,name,age,student_id):
        super().__init__(name,age)
        self.student_id = student_id

    def __str__(self):
        return f"Student: name = {self.name} ; age = {self.age} ; student_id = {self.student_id}"

myObj = Student("John", -1, 4567564)
print(myObj)
