marks=[10,20,30,40,50]
print(marks)
print(len(marks))
print(type(marks))

student = ["Nafis",2007075,"CSE"]
print(student)
print(student[0])
print(student[1])
print(student[2])
student[0]="KUET"
print(student)

student.append("2K20")

print(student)

list = [5,4,3,2,1]
list.sort() #sorting acending order
print(list)

list.sort(reverse=True) #sorting decending order
print(list)

str = ['d','s','t','b','o','s','e']
str.sort()
print(str)

str.sort(reverse=True)
print(str) 

list = [2,1,3]
list.insert(1,5) # insert value 5 in the index no 1
print(list) 

list.remove(1) #remove the first occurance of 1
print(list)

list.pop(0) #remove element from index no 0
print(list)

#palindrome and non-palindrome checking

list1 = [1,2,1]
list2 = [1,2,3]

cpy_list1=list1.copy()
cpy_list2 = list2.copy()

cpy_list1.reverse()
cpy_list2.reverse()

if(list1==cpy_list1):
    print("List-1 is a palindrome")
else:
    print("List-1 is not palindrome")

if(list2==cpy_list2):
    print("List-2 is a plindrome")
else:
    print("List-2 is not palindrome")