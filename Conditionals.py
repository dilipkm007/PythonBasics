#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 15 21:26:52 2023

@author: Dilip Kumar
"""

#Boolean expressions
print("Example of Boolean expressions")
print("3 == 3", 3 == 3)
print("3 < 3", 3 < 3)
print("3 > 3", 3 > 3)
print("3 != 3", 3 != 3)
print("3 <= 3", 3 <= 3)
print("3 >= 3", 3 >= 3)
print("")
print("3 == 2", 3 == 2)
print("3 < 2",3 < 2)
print("3 > 2",3 > 2)
print("3 != 2", 3 != 2)
print("3 <= 2", 3 <= 2)
print("3 >= 2", 3 >= 2)
print("Type of true:", type(True))
print("")

#Logical Operators
print("Example of Logical Operators")
print("True and True", True and True)
print("True and False", True and False)
print("True or True", True or True)
print("True or False", True or False)
print("")
v1, v2, v3 = 15, 20, 25
print("(", v1, "and", v2, "< 100 ) =", (v1 < 100 and v2 < 100))
print("(", v2, "and", v3, "< 22 ) =", (v2 < 22 and v3 < 22))
print("(", v2, "or", v3, "< 22 ) =", (v2 < 22 or v3 < 22))
print("")
print("True=", True)
print("not True=", not True)
print("False=", False)
print("not False=", not False)
print("not(", v1, "and", v2, "< 100 ) =", not(v1 < 100 and v2 < 100))
print("not(", v2, "and", v3, "< 22 ) =", not(v2 < 22 and v3 < 22))
print("not(", v2, "or", v3, "< 22 ) =", not(v2 < 22 or v3 < 22))


#If else conditions
print("")
print("Example of If-else statements")
some_condition = True
if some_condition:
    print('The variable \'some_condition\' is True')
else:
    print('The variable \'some_condition\' is False')

temp = int(input("Please enter the temprature in celsius(℃). \n An integer between 0-40:>>> "))
if temp > 30:
    print("Wear shorts and sum cream!")
elif temp <= 30 and temp > 20:
    print('It\'s warm, but not shorts wwather!')
elif temp <= 20 and temp > 10:
    print('You\'ll probably need a vest today!')
else:
    print('Too cold! Don\'t go out!')
    
    
