#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 17 20:57:53 2023

@author: DIlip Kumar
"""

## Problem:1
'''
    Write code that asks user to input a number between 1 and 5 inclusive.
    The code will take the integer value and print the string value. So 
    for example if user input 2 the code will print 'two'. Reject any input that 
    is not a number in the range

'''
num = int(input("Enter number between 1 and 5 inclusive :>>> "))
if num == 1:
    print("one")
elif num == 2: 
    print("two")
elif num == 3: 
    print("three")
elif num == 4: 
    print("four")
elif num == 5: 
    print("five")
else:
    print("Number not in given range")
    
    
## Problem:2
'''
    Write code that asks user to input a number string between one and five inclusive.
    The code will take the string value and print the Number value. So 
    for example if user input one the code will print '1'. Reject any input that 
    is not a number string in the range

'''

strNum = input("Enter the number string between one and five:>>> ")
strNum = strNum.lower()
if strNum == 'one':
    print("1")
elif strNum == 'two':
    print("2")
elif strNum == 'three':
    print("3")
elif strNum == 'four':
    print("4")
elif strNum == 'five':
    print("5")
else:
    print("Entry not in valid range")
    
    
    
## Problem:3
'''
    User guess number between 1-10
    if it guess correct  "You win"
    if less than numer say "You guess too low sorry you loss"
    if greater than numer say "You guess too high sorry you loss"
    else out or range selection

'''
theSecret_num = 9
guess = input("Please guess numer between 1-10 :>>> ")
if guess.isdigit():
    if num == theSecret_num:
        print("Hurre! You win 🎉")
    elif num < theSecret_num and num >= 1:
        print("Sorry! You lost😑 you guess is too low")
    elif num > theSecret_num and num <= 10:
        print("Sorry! You lost😑 you guess is too high")
    else:
        print("Number not in range❌")
else:
   print("Please enter a number🙏")

## Problem:4 

'''
    User Enter his/her name
    tell them length of name if charater more than 5
    else its seceret
    

'''

name = input("Please🙏 Enter your name :>>> ")
length = len(name)
if length > 5:
    print('Your name contains', length, 'characters')
else:
    print('I\'m not tellling the length of your name.')

## Problem:5
'''
Take two input from user as number 
if both num > 15 product it
if one > 15 sum it
else return zero
'''

num1 = int(input("Enter first number for mathematics :>>> "))
num2 = int(input("Enter Second number for mathematics :>>> "))
if num1 > 15 and num2 > 15: 
    print("The product of", num1, 'and', num2, 'is', num1 * num2)
elif num1 > 15 or num2 > 15: 
    print("The sum of", num1, 'and', num2, 'is', num1 + num2)
else:
    print(0)


## Problem:6
'''
Take two input from user as number 
and swap it
'''
num1 = int(input("Enter first number for swap :>>> "))
num2 = int(input("Enter Second number for swap :>>> "))
print("Before swap num1=", num1, 'and num2=', num2)
num1, num2 = num2, num1
print("Before swap4 num1=", num1, 'and num2=', num2)
