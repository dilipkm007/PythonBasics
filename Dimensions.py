#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 21:41:32 2023

@author: Dilip Kumar
"""

my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] #2d List
print("Fist elements:", my_list[0])
print("Fist elements:", my_list[1])
print("Fist elements:", my_list[2])
print("Access 9:", my_list[2][2])


##With Dict
countries = { 'France': {'Capital': 'Paris', 'Language': 'French'}, 'UK': {'Capital': 'London', 'Language': 'English'},  'India': {'Capital': 'New Delhi', 'Language': 'Hindi'} }

print(countries['France'])
print(countries['France']['Language'])
print()
for key, value in countries.items():
    print(key, value)
print()

for key, value in countries.items():
    print(f'{value["Capital"]} is the capital of {key}, they speak {value["Language"]}.')
    

