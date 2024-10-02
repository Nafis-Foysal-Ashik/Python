tuple = (2,1,3,1)
print(type(tuple))
print(tuple)
print(tuple[0])

#tuple[0]=5 #it will give an error because it's possible in list not in tuples

tuple = (0,)
print(type(tuple)) # tuple
tuple=("Nafis",)
print(type(tuple)) #tuple

tuple = (0)
print(type(tuple)) #integer
tuple=("Nafis")
print(type(tuple)) #string

tuple = (4,2,3,1,2,1,2)
print(tuple.index(2)) #returns the index no of first occurance of element 2
print(tuple.count(1)) 

movies = []

m1 = input("Enter 1st movie : ")
m2 = input("Enter 2nd movie : ")
m3 = input("Enter 3rd movie : ")

movies.append(m1)
movies.append(m2)
movies.append(m3)

print(movies)