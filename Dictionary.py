student_info={
    "key":"value",
    "name":"Nafis",
    "id":2007075,
    "Dept":"CSE",
    "University":"KUET",
    "Course":["Structure Programming","Object oriented programming","Data structure"],
    "Code":("CSE-3100","CSE-3200","CSE-3112")
}

print(student_info["name"])

student_info["name"]="Ashik"
print(student_info)

student_info["Address"]="Khulna"
print(student_info)

#nested dictionary

student_result = {
    "name":"Nafis",
    "id":2007075,
    "subject":{
        "C Programming":"A",
        "C++":"A-",
        "Math":"A+",
    }
}

print(student_result)
print(student_result["name"])
print(student_result["subject"])
print(student_result["subject"]["Math"])

print(student_result.keys()) #return all the keys
pairs = list(student_result.keys()) #type cast into list 
print(len(student_result))
print(pairs)

print(student_result.values()) #return all the values
pairs =list(student_result.values()) #type case into list
print(pairs)

print(student_result)
print(student_result.items())
pairs = list(student_result.items())
print(pairs)
print(pairs[0])
print(pairs[1])
print(pairs[2])

print(student_result["name"])
print(student_result.get("name"))

#print(student_result["name2"]) #will give error
print(student_result.get("name2")) #will return none value

student_result.update({"Dept":"CSE"})
print(student_result)

address = { "Address":"Khulna",
            "Division":"Khulna",
            "District":"Chuadanga"
            }

student_result.update(address)
print(student_result)
print(student_result.items())


#problem question 

#i/p 3 sub marks and print them in a dictionary

marks={}

x = int(input("Math : "))
y = int(input("Physics : "))
z = int(input("English : "))

marks.update({"Math " : x})
marks.update({"Engilsh " : y})
marks.update({"Physics " : z})

print(marks)
