class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

ob1 = MyClass("Abdullah", 18)

#Modifying Object Properties
ob1.age = 19

print(ob1.age)

#Delete a Property
del ob1.age


#Delete object
del ob1

#print(ob1.age)