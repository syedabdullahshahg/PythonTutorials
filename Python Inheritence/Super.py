class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name: "  + self.name)
        print("Age: " + str(self.age))

class Student(Person):
    def __init__(self, name, age, dep):
        super().__init__(name, age)
        self.dep = dep

    def display(self):
        super().display();
        print("Department: " + self.dep)

stu1 = Student("Abdullah", 19, "BS IT")

stu1.display()