class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Display(self):
        print("Name of Student is: " + self.name)
        print("Age of Student is: " + str(self.age))

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

ob1 = Student("Abdullah", 19)

ob1.Display()

ob1.setName("Shah")
ob1.setAge(18)

ob1.Display()