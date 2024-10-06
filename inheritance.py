#single inheritance

class Car:
    @staticmethod
    def start():
        print("Car started...")
    
    @staticmethod
    def stop():
        print("Car stopped...")

    def __cost(self , amount):
        print("Cost is : " , amount)
    def get_cost(self , amount):
        self.__cost(amount)

class Toyota(Car):
    def __init__(self ,name):
        self.name = name
    

car1 = Toyota("Fortuner")
print(car1.name)

car1.start()
car1.get_cost(10000)
car1.stop()

#multi-level inheritance
class Teacher:
    def __init__(self , name):
        self.name = name

    @staticmethod
    def designation(condition):
        print("Teacher ",condition )
    @staticmethod
    def salary(salary):
        print("Salary : ",salary )

class Address(Teacher):
    # def __init__(self , address):
    #     self.address = address
    
    def __init__(self , name , address ):
        self.address = address
        super().__init__(name)

x = Address("Nafis" , "Chuadanga")
print(x.address)
print(x.name)
x.salary(10000)


class Complex:
    def __init__(self , real , img):
        self.real = real
        self.img = img

    def show(self):
        print(self.real ,"+" ,self.img,"i")

    def add(self , num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newImg , newImg)
    
    def __add__(self , num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newImg , newImg)
    
    def __sub__(self , num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newImg , newImg)
    
    def __mul__(self, num2):
        newReal = (self.real * num2.real) - (self.img * num2.img)  
        newImg = (self.real * num2.img) + (self.img * num2.real)   
        return Complex(newReal, newImg)
    
    def __truediv__(self , num2):
        denom = num2.real**2 + num2.img**2  
        newReal = (self.real * num2.real + self.img * num2.img) / denom  
        newImg = (self.img * num2.real - self.real * num2.img) / denom  
        return Complex(newReal, newImg)

num1 = Complex(1,3)
num1.show()

num2 = Complex(4,6)
num2.show()

num3 = num1.add(num2) # revoke add()
num3.show()

num4 = num1 + num2 #revole __add__
num4.show()

num5 = num1 - num2 #revole __sub__
num5.show()

num6 = num1 * num2 #revoke __mul__
num6.show()

num7 = num1 / num2 
num7.show()

