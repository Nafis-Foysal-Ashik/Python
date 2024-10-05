class student:
    name = "Nafis"
    id = 2007075
    dept = "CSE"
    versity = "KUET"

s1 = student()
print(s1.name ," " ,s1.id," ",s1.dept," ",s1.versity)

#constructor

class Student:

    #common attribute section for every object
    #class attribute
    college_name="Chuadanga Govt College"

    #default constructor
    # def __init__(self):
    #     pass

    #object attribute

    def __init__(self , fullname , marks):
        self.name=fullname
        self.mark = marks
        print("Adding new student...")

s1 = Student("Nafis" , 90)
print(s1.name , s1.mark)

s2=Student("Foysal" , 100)
print(s2.name , s2.mark)

print(s1.college_name)
print(s2.college_name)

#method

class Person:
    def __init__(self , name , roll):
        self.name = name
        self.roll = roll

    def welcome(self):
        print("Welcome ,",self.name)
    
    def get_roll(self):
        print("Roll -> ",self.roll)

x = Person("Nafis",75)
x.welcome()
x.get_roll()

#Practise Problem

class Result:
    def __init__(self , name , marks):
        self.name = name
        self.marks=marks

    @staticmethod
    def result():
        print("Hello World")

    def cal_avg(self):
        sum=0
        for mark in self.marks:
            sum+=mark
        print("Name : ",self.name , "Your avg marks is : ",sum/3)

x = Result("Nafis" , [100,90,80])
x.cal_avg(); 
x.result()


class Bank:
    def __init__(self , name , acc_no , balance):
        self.name = name
        self.account_no = acc_no
        self.balance = balance
    
    def debit(self , amount):
        self.balance -= amount
        print(amount , " Taka is Debited")
    
    def credit(self , amount):
        self.balance += amount
        print(amount , " Taka is Credited")

    def get_bal(self):
        print("Current Balance is : " , self.balance)
    
x = Bank("Nafis" , 1212 , 10000)
x.debit(100)
x.get_bal()

x.credit(1050)
x.get_bal()
