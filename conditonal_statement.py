"""mark = int(input("Enter your mark : "))

if(mark>=80):
    print("You got A+")
    print("Your grade is A+")
    print("Congratulations")
elif(mark>=70 and mark<80):
    print("You got A")
    print("Your grade is A")
    print("Congratulations")
elif(mark>=60 and mark<70):
    print("You got A-")
    print("Your grade is A-")
    print("Congratulations")
else:
    print("You got F")
    print("Your grade is F")
    print("Fuck You")"""

#true or false print

a = int(input("enter first number : "))
b = int(input("Enter secont number : "))

print(a>=b)

#ternerary conditional operator

"""food=input("food : ")
eat="Yes" if food == "cake" else "no"
print(eat)

food = input("food : ")
print("sweet") if food=="cake" or food=="jalebi" else print("not sweet")"""

#Claver if

age = int(input("age : "))
vote = ("yes","no") [age>=18] #true = index 1 means no will be printed
print(vote)
age = int(input("age : "))
vote = ("yes","no") [age>18] #false = index = 0 means yes will be printed
print(vote)


salary = int(input("salary : "))
tax = ((0.1*salary) , (0.5*salary)) [salary>50000]
print(tax) 