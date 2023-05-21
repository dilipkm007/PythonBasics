#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 03:53:29 2023

@author: Dilip Kumar
"""

'''
Problem 1: How to check if a key exists in dictionary 
            Take user input for country and check if key existes in dict
'''

capitals = {"India": 'New Delhi', 'Fance': 'Paris', 'Spain': 'Madrid', 'United Kingdom': 'London',
            'United States': 'Washington DC', 'Italy': 'Rome', 'Denmark': 'Copenhangen',
            'Germany': 'Berlin', 'Greece': 'Athens', 'Bulgaria': 'Sofia', 'Ireland': 'Dublin',
            'Maxico': 'Mexico City'}

user_input = input('Which country would you like to check? ')
user_input = user_input.lower()

while ('united kingdom' not in user_input and not user_input.isalpha()):
    if user_input == 'united states':
        break
    print('You must enter a string')
    user_input = input('Which country would you like to check? ')

user_input = user_input.title()

if user_input in capitals:
    print(f'The capital of {user_input} is {capitals[user_input]}')
else:
    print(f"Sorry try again! The country \'{user_input}\' not in the list.")



'''
Problem 2: Write a dictionary, with Key: the position of digit in Fibonacci serriece and value: the value of that position first 12 digits
{1:0, 2:1, 3:1, 4:2, 5:3, 6:5, 7:8  ....}
'''


n = 12
a = 0
b = 1
d = {}
for i in range(1, n+1):
    d[i] = a
    a,b = b, a+b
print(d)



'''
Problem 3: Create a dictionary to represent the open, high, low, close share price data
for 4 imaginary companies. 'Python DS', 'PythonSoft', 'Pythazon', 'Pybook'
the 4 sets of data are [12.87, 13.23, 11.42, 13.10], [23.54, 25.76, 12.87, 22.33], [98.99, 102.34, 97.21, 100.065], [203.63, 207.54, 202.43, 205.24]

'''

dict1 = dict()
keys_name = ['open', 'high', 'low', 'close']
companies = ['Python DS', 'PythonSoft', 'Pythazon', 'Pybook']
prices = [[12.87, 13.23, 11.42, 13.10], [23.54, 25.76, 12.87, 22.33], [98.99, 102.34, 97.21, 100.065], [203.63, 207.54, 202.43, 205.24]]
for i in range(len(keys_name)):
    dict1[companies[i]] = dict(zip(keys_name, prices[i]))
print()
print(dict1)


'''
Problem 4: Implements any python module
'''

import datetime

today = datetime.date.today()
print()
print(f'Today\'s date is {today}.')
holiday = datetime.date(2023, 10, 31)
delta = holiday - today
print(f'just {delta.days} days until the holidays!')


'''
Problem 5: Create a dictionary containing as keys the letter from A-Z, the value should be random numbers
created from the random module. Also plot this on bar graph.
'''
import random

keys = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

dict_new = dict()

for letter in keys:
    dict_new[letter] = random.randint(1, 100)
print()
print(dict_new)

import matplotlib.pyplot as plt

x,y = zip(*dict_new.items())
plt.bar(x,y)
plt.show()


'''
Problem 6: Create a dictionary containing 4 suits of cards ['Ace', 2, 3, 4, 5 ,6 ,7, 8, 9, 10, Jake, Queen, King]

'''

suites = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jake', 'Queen' 'King']
dict_cards = dict()
for suite  in suites:
    dict_cards[suite] = ranks
print()
print(dict_cards)