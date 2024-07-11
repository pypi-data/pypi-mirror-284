import math as m

def val(n,p):
    i=1
    while True:
        if n%(p**i) != 0:
            return i-1
            break
        elif n==0:
            return -1
        i+=1

def is_prime(n):
    if n>=3:
        r=1
        for i in range(2,n):
            if n%i == 0:
                r = 0
                break
        return r
    elif n == 2:
        return 1
    elif n == 1 or n==0:
        return 0

def is_sqrt(n):
    if int(m.sqrt(n)) == m.sqrt(n):
        return 1
    else:
        return 0
    