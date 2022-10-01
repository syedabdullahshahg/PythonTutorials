class Aver:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def getAver(self):
        sum = self.num1+ self.num2+self.num3
        aver = sum/3
        return aver

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))

ob1 = Aver(n1, n2, n3)

print("Average of these 3 number is: " + str(ob1.getAver()))
