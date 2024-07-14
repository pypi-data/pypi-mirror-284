import math as m
import matplotlib.pyplot as plt
import numpy as np

def plot(function,min,max,speed=0,verbose=False,color="blue",show=True,fig=0):
    x_values=[]
    y_values=[]
    
    if fig != 0:
        plt.figure(fig)

    for i in range(min,max+1):
        x_values.append(i)
        y_values.append(function(i))
        if verbose:
            print(i,function(i))
        if i <= max - 1:
            plt.plot(x_values,y_values,c=color)
        elif i == max:
            plt.plot(x_values,y_values,c=color,label=function.__name__)
        if speed != 0:
            plt.pause(speed)
    if show:
        plt.legend()
        plt.show()

def poly_plot(functions_list,colors_list,min,max,distinct=False):
    if distinct:
        for i in range(len(functions_list)):
            plot(functions_list[i],min,max,color=colors_list[i],show=False,fig=i+1)
            plt.legend()
        plt.show()
    else:
        for i in range(len(functions_list)):
            plot(functions_list[i],min,max,color=colors_list[i],show=False)
            plt.legend() 
        plt.show()    


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
    
def euler_totient(n):
    result = n 
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

def mobius_function(n):
    if n == 1:
        return 1
    for k in range(2, int(n**0.5) + 1):
        if n % (k * k) == 0:
            return 0
    prime_count = 0
    num = n
    for i in range(2, n + 1):
        if num % i == 0:
            prime_count += 1
            while num % i == 0:
                num //= i
        if num == 1:
            break
    if prime_count % 2 == 0:
        return 1
    else:
        return -1

def prime_counting(n):
    prime = [True] * (n+1)
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    count = 0
    for p in range(2, n+1):
        if prime[p]:
            count += 1
    return count

def prime_omega(n):
    distinct_prime_factors = set()
    while n % 2 == 0:
        distinct_prime_factors.add(2)
        n = n // 2  
    for i in range(3, int(m.sqrt(n)) + 1, 2):
        while n % i == 0:
            distinct_prime_factors.add(i)
            n = n // i
    if n > 2:
        distinct_prime_factors.add(n)
    
    return len(distinct_prime_factors)

def tau(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i == n // i:
                count += 1
            else:
                count += 2
    return count

def sigma(n):
    sum_divisors = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            sum_divisors += i
            if i != n // i:
                sum_divisors += n // i
    return sum_divisors