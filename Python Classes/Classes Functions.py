class MyClass:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Intro(self):
        print("Hello My Name is: " + self.name)
        print("My age is: " + str(self.age))

Obj = MyClass("Abdullah", 19)

Obj.Intro()