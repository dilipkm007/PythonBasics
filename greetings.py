#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 04:35:28 2023

@author: Dilip Kumar
"""





def fibonacci_2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_2(n-2) + fibonacci_2(n-1)



def fibonacci(n):
    ''' Calculate and  return fibonacci number'''
    a = 0
    b = 1
    for i in range(n):
        a, b = b, b + a
    return a
        