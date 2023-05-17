#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 17 05:09:18 2023

@author: Dilip Kumar
"""

my_String = "Python"
print("'" + my_String + "'\'s length is", len(my_String))
print("In '" + my_String + "' at 0th position/ First character", my_String[0])
print("In '" + my_String + "' at 1st position/ Second character", my_String[1])
print("In '" + my_String + "' at 0th(include) to 4th(not include) position", my_String[0:4])
print("In '" + my_String + "' at start to 4th(not include) position", my_String[0:4])
print("In '" + my_String + "' at start to 4th(not include) position", my_String[:4])
print("In '" + my_String + "' at start from 1st to end position", my_String[1:])
print("In '" + my_String + "' Last character", my_String[-1])
print("In '" + my_String + "' Second Last character", my_String[-2])

#we can store letter 
letter = my_String[4]
print("letter at 4th position:", letter)
print("")
print(my_String, "to upper case: ", my_String.upper())
print(my_String, "to lower case: ", my_String.lower())

#Game
word = 'summer'
guess = input("I'm thinking of a word, can you guess what it is? Hint: It's a season. :>>> ")
guess = guess.lower()

if guess == 'summer':
    print("Oh Yes, It's Summer: well done! +1")
elif guess == 'winter':
    print("Oh No, It's not Winter: Sorry! -1")
elif guess == 'autumn':
    print("Oh No, It's not Autumn: Sorry! -1")
elif guess == 'spring':
    print("Oh No, It's not Spring: Sorry! -1")
else: 
    print("Are you Joking , It's(", guess.capitalize(), ")not a season: Sorry! -1")