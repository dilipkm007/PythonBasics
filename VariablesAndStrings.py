#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 15 19:18:36 2023

@author: Dilip Kumar
"""

#Memory space --> Integer, Float, Bool, String --> Variable Name
x = 5
y = 12
#Memory space --> value(x+y) ->> z
z = x + y
print(x," + ", y, " = ", z)

z = x - y
print(x," - ", y, " = ", z)

#Variable should have meaning full name
a = 2.5
b = 3.14159
c = b * a**2
print("c =", c)
#instead we use meaning full name
radius = 2.5
PI = 3.14159
area = PI * radius**2
print("area of circle = ", area)



## Strings

phrase_1 = 'The cat sat on the mat!'
phrase_2 = 'And so did the dog!'
phrase_3 = phrase_1 + ' ' + phrase_2
print(phrase_3)


##Take input from user
user_input = input("How many apples do you have? \n >>> ")
print("Value = ", user_input, "\tType = ", type(user_input))
user_input_int = int(user_input)
##if user_input othere than number string it will crash
print("Value = ", user_input_int, "\tType = ", type(user_input_int))

##Keywords
#help()
## help> keywords you will get all list of keywords use quit to return from help to actual console

#Variable name as keyword YOu will get compile error
# while = 5

## Problem 1:
    #Ask user to input th radius of circle and give output area
    
radius = float(input("What is radius of circle?\n only Numbers 5  >>> "))
PI = 3.141519
circle_area = PI * radius ** 2
print("The area of circle for given", radius, "radius: = ", circle_area)


## Problem 2:
    #convert fahrenheit to celsius
fahrenheit = float(input('Please enter the temprature in fahrenheit: \n Only Numbers >>> '))
celsius = (fahrenheit - 32) * (5/9)
print("You entered fahrenheit:", str(fahrenheit) +  "℉", "so the temprature in celsius is:", str(celsius) + "℃ \n")

## Problem 3: 
    #Sum of two integer take input from user

input_one = int(input("Plase enter first number you want to add: Only Integer >>> "))
input_two = int(input("Plase enter second number you want to add: Only Integer >>> "))
sum = input_one + input_two
print("The sum of", input_one, 'and', input_two, 'is', sum)



## Problem 4: 
    #Product of two integer take input from user

input_one = int(input("Plase enter first number you want to product: Only Integer >>> "))
input_two = int(input("Plase enter second number you want to Product: Only Integer >>> "))
product = input_one * input_two
print("The product of", input_one, 'and', input_two, 'is', product)

## Problem 5
#Bob, Ann, Jane and Ashwin wants the to order Pizza - they know they will each it 4 slices of pizza.
#The local pizza shop sells pizza of only 6 slices.
#what is minimum #Pizza needed use floor division 
needSlices = 4 * 4
pizzaHaveSilices = 6
##5 == 6-1 which make sure we get next whole number
requiredPizza = (needSlices + 5) // pizzaHaveSilices
numberOfSlicesLeft =  requiredPizza * 6 - needSlices
print(r"Number of pizza required:", requiredPizza, "Number of slices left after eat pizza:", numberOfSlicesLeft)

