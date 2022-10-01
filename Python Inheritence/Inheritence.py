class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name: " + self.name)
        print("Age: " + str(self.age))

class Student(Person):
    pass

stu1 = Student("Abdullah", 19)

stu1.display()