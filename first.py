print("hello world","My name is Nafis")
print("Hello world.")
print("My name is Nafis") #to print different line

#variables
name="Nafis"
age=22
price=29.99
old=True
a=None

print(name)
print(age)
print(price)

print("My name is ",name , ". My age is ",age , ". My book price is " ,price)

#type
print(type(name))
print(type(age))
print(type(price))
print(type(old))
print(type(a))

#expression execution
x,y=2,3 # x=2 y=3
txt="@"
print(x*txt*y)

x,y="2",3
txt="@"
print((x+txt)*y)

#normal division
a,b=3,2
c=a/b
print(c)

#integer division

a,b=7,2
c=a//b
print(c) #print the floor value of the float number

a,b=-7,2
c=a//b
print(c)

a,b=7,-2
c=a//b
print(c)

#remainder operator
a,b=10,3
c=a%b
print(c) #10%3=10−(10//3)×3=10−3×3=10−9=1

a,b=-10,-3
c=a%b
print(c) #−10%−3=−10−(−10//−3)×−3=−10−3×−3=−10−(−9)=−10+9=−1

a,b=10,-3
c=a%b
print(c) #10%−3=10−(10//−3)×−3=10−(−4)×−3=10−12=−2

a,b=-10,3
c=a%b
print(c) #−10%3=−10−(−10//3)×3=−10−(−4)×3=−10+12=2

# multi line comment

"""This is a multi line 
commetn 
okey bro
do you understand 
this
"""
#input
#name = input("name : ")
#print(name) #input function by default take all the value in string fromat

# input type caseting

"""age = int(input("age: "))

price = float(input("price : "))

print("Your age is : ",age)
print("Your price is : ",price)"""

#bit-wise operator

a,b=1,2

c=a^b
print(c)

c=a&b
print(c)

c=a|b
print(c)