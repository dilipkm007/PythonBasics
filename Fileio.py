#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 05:24:00 2023

@author: Dilip Kumar
"""

# f = open('kipling.txt', 'w')
# print(type(f))
# f.write('If you can keep your head while all about you \nare loosing theirs \
# and blaming it on you,\n')
# f.write('If you can trust yourself when all men doubt you,\n\
# But make allowance for their doubting too;\n')
# f.write('If you can wait and not be tired by waiting,\n\
# or being lied about, don\'t deal in lies,\n')
# f.write('or being hated, don\'t give way to hating\n\
# and yet don\'t look too good, nor talk too wise:\n')
# f.close()


# f = open('kipling.txt', 'r')
# # print(type(f))
# # print(f.read())
# # print(f.readline())
# con = f.readlines()
# print(con)
# print(type(con))
# f.close()



f = open('kipling.txt', 'a')
f.write('If you can dream - and not make dreams your master;\n\
if you can think - and not make thoughts your aim;\n')
f.close()
print()

f = open('kipling.txt', 'r')
print(f.read())
f.close()
print()

#This will automatic close file
with open('kipling.txt', 'r') as f:
    for line in f.readlines():
        print(line, end='')
        

#Functions
def hello():
   return 'Hello World!'
    
for i in range(5):
    print(hello())

def hello(name):
    print('Hello', name+".")
    
hello('Dost')


def hello_2(name="Mitra"):
    print(f'Hello {name}')

hello_2('Dostar')


## Fibonacci Sequence 
def fibonacci(n):
    ''' Calculate and  return fibonacci number'''
    a = 0
    b = 1
    for i in range(n):
        a, b = b, b + a
        # print(a)
    return a
        

last = fibonacci(20)
print("last:", last)

def calc_min(first, *remainder):
    '''
        This is calculate mean of numbers of parameter, int
    '''
    mean = (first + sum(remainder))/ (1 + len(remainder))
    return mean
print(calc_min(23, 43, 56, 76, 45, 34, 65, 75, 975, 3456, 54))

print()
def fibonacci_2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_2(n-2) + fibonacci_2(n-1)

import timeit
t1 = timeit.Timer("fibonacci(36)", "from greetings import fibonacci")
print(t1.timeit(5))
print()
t2 = timeit.Timer("fibonacci_2(36)", "from greetings import fibonacci_2")
print(t2.timeit(5))
