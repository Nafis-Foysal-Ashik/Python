def rec_num(n):
    if(n==0):
        return
    else:
        print(n)
    rec_num(n-1)

rec_num(10)


#factorial

def rec_fact(n):
    if(n==0):
        return 1
    else:
        return n * rec_fact(n-1)

x = rec_fact(5)
print(x)

def print_list(list , idx):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list , idx+1)

num = [1,2,3,4,5,6,7]
print_list(num,0)
