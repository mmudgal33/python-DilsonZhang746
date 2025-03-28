# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 12:45:46 2022
Mathematics and Linear Algebra using Python 

@author: https://www.youtube.com/@easydatascience2508
"""

### Tutorial 1. Finding n-th Fibonacci number using Python

#define a function
def Fib(n):
    if n<= 0:
        print("n should be at least 1")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fib(n-1)+Fib(n-2)
 
    
print(Fib(7))



#using list
FibList = [0, 1]
 
def fib(n):
    if n<0:
        print("n should be at least 1")
    elif n<= len(FibList):
        return FibList[n-1]
    else:
        temp_fib = fib(n-1)+fib(n-2)
        FibList.append(temp_fib)
        return temp_fib
 
print(fib(7))