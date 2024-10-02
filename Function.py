def cal_sum(a , b):
    sum = a+b
    print(sum)

cal_sum(5,10)

cal_sum(10,20)

cal_sum(25,10)

def cal_mul(a , b):
    mul = a*b
    return mul

x = cal_mul(5,10)
print(x)

y = cal_mul(10,20)
print(y)

z = cal_mul(25,10)
print(z)


#parameter
def cal_sum(a=2 , b=3):
    sum = a+b
    print(sum)

cal_sum()

def cal_sum(a , b=5):
    sum = a+b
    print(sum)

cal_sum(1)

cities = ["Dhaka" , "Khulna" , "Sylhet" , "Chottogram"]
heroes = ["Ironman" , "CaptainAmerica" , "Thor" , "Hulk" , "Groot"]

def fun_len(list):
    print(len(list))

fun_len(cities)
fun_len(heroes)

def fun_ele(list):
    for item in list:
        print(item , end=" ") # end = " " is used to print in the same line
    print()

fun_ele(cities)
fun_ele(heroes)

#factorial

def fun_fact(n):
    factorial = 1
    for i in range(1 , n+1):
        factorial*=i
    print(factorial)

fun_fact(5)