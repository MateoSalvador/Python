# -*- coding: utf-8 -*-
"""
@author: christian
"""

#Factorial of a number
def factorial(n):
    fact = 1
    for factor in range(n,0,-1):
        fact = fact * factor
    return fact

factorial(100)


#Fibonnacci of a number
def fib1(n):    # this function cannot compute fib(100)
    if n==1:
        return 1
    if n==0:
        return 0
    return fib1(n-1) + fib1(n-2)

fib1(20)

def fib2(n):
    a, b = (0, 1) #tuple
    for i in range(1,n+1):
        a, b = (b, a + b) #tuple
    return a

n = 100
if n<15:
    print(fib1(n))
else: 
    print(fib2(n))

