#set are unordered 

collection = { 1,2,3,4,"Hello","World"}
print(collection)
print(len(collection))


collection={1,2,2,3,3,4,"Hello","World","World"} #remove the duplicate value 
print(collection)
print(len(collection))

collection = {}
print(type(collection))

collection = set()
print(type(collection))
print(collection)

collection.add(1)
collection.add(2)
collection.add("Hello World")
print(collection)

collection.remove(2)
print(collection)

collection.clear()
print(len(collection))

collection = {"Hello" , "World" , "Nafis" , "Foysal" , "Ashik"}
print(collection) 

collection.pop() #delete any random element
print(collection)

collection.pop() #delete any random element
print(collection)

#union operation

set1={"Name" , "ID" , "Dept"}
set2={"Nafis" , "2007075" , "CSE"}

set3=set1.union(set2)
print(set3)
print(set1)
print(set2)

#intersection operation
set1={1,2,3,4}
set2={2,3,4,5}
set3=set1.intersection(set2)
print(set3)

value={9,9.0}
print(value)

value={"9.0" , 9}
print(value)

value={
    ("float",9.0),
    ("int",9)
}
print(value)