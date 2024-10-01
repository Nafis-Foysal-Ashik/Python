#string declaration
str1="Nafis"
str2='Foysal'
str3="""Ashik"""

print(str1,str2,str3)

str="My name is Nafis .\nMy age is 22"
print(str)

#concatination

str1="Dipesh"
str2="Gab"
str3=str1+str2
print(str3)

print(len(str3))

#string slicing

str="hello world"
str1=str[1:5] #index 1 to 5
print(str1)
str2=str[:len(str)] #index 0 to length of the string
str3=str[5:] #index 5 to length of the string

str = "Apple"
"""
A=-5
p=-4
p=-3
l=-2
e=-1

"""

str1= str[-3:-1]
print(str1)

#string function

str="i am a coder"

print(str.endswith("er"))
print(str.capitalize())
print(str)
str=str.capitalize()
print(str)

print(str.replace("a","jani"))

print(str.find("m"))

print(str.count("a"))