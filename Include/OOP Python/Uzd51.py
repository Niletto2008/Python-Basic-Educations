"/ Uzd6 /"
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
        
    def info(self):
        print("Person: name = {self.name} ; age = {self.age} ")

class Student(Person):
    def __init__(self,name,age,student_id):
        super().__init__(name,age)
        self.student_id = student_id

    def info(self):
        print("Student: name = {self.name} ; age = {self.age} ; student_id = {self.student_id}")

myObj1 = Person("John", 18)
myObj2 = Student("Jack", 23, 567567)
x = [myObj1, myObj2]
for y in x:
    y.info()

"/ Uzd7 /"

class Animal:
    def __init__(self):
        self.dog = self.Dog()
        self.cat = self.Cat()
    def make_sound(self):
        return f"Animal says many soynds!"
    class Dog:
        def make_sound(self):
            print("Dog say GAV GAV GAV!")
    class Cat:
        def make_sound(self):
            print("Dog say MEOW MEOW MEOW!")

anim = Animal()
dog = anim.Dog()
dog.make_sound()
cat = anim.Cat()
cat.make_sound()