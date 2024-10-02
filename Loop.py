#while loop

count = 1

while count<=5:
    print("Hello World")
    count+=1

#print multiplication

count = 1

print("Enter number : ")
while count<=10:
    print(3*count)
    count+=1

nums = ( 1,2,3,4,5,6,7,8,9 )

x = 5

idx=0

while idx < len(nums) : 
    if(nums[idx]==x):
        print("Found at index : ",idx)
    idx+=1


#for loop

num = [1,2,3,4,5,6,7,8,9,0]

for i in num:
    print(i)

str="Nafis Foysal Ashik"
for c in str:
    print(c)

for idx in num:
    if(idx==5):
        print("Found at index : ",idx-1)
        break

#range

sec = range(10) #range(stop)
print(sec)

for i in sec:
    print(i)

#range(start , stop)

sec = range(2,10)
for i in sec:
    print(i)

#range(start , stop , step_size)
sec = range(2,10,2)
for i in sec:
    print(i)


sec = range(100 , 0 , -1)
for i in sec:
    print(i)

for i in range(6):
    pass # pass is used for future expansion

num = range(11)
sum=0
for i in num:
    sum+=i

print(sum)

#factorial
sum=1
for i in range(5):
    sum*=i+1

print(sum)