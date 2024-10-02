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