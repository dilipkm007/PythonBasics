#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 04:31:43 2023

@author: Dilip Kumar
"""

## Loops
# For Loop
#for(stop) start from 0
for i in range(10):
    print(i)
print()

for i in range(10):
    print(i, end=" ")
print()

#for(start, stop)
for i in range(1, 10):
    print(i, end=" ")
print()

for i in range(1, 11):
    print(i, end=" ")
print()

#help(range)

#for(start, stop, steps)
for i in range(0, 101, 4):
    print(i, end=" ")
print()

#for(start, stop, steps) reverse
for i in range(100, -1, -4):
    print(i, end=" ")
print()

# Another way for loop without range
word = 'Python'
for char in word:
    print(char, end=" ")
print()



#more on variables
print()
x = 5
x = x + 1
print('x=', x)
x += 1
print('x=', x)
y = x
print('y=', y)
x += 1
print('x=', x)
print('y=', y)
x = 5


#Lists

#empty list
data1 = []

#List with value
data = [53, 76, 25, 98, 56, 42, 69, 81]
print("List", data)
print("List first element at indext 0:", data[0])
print("List third element at indext 2:", data[2])
print("List sixth element at indext 5:", data[5])
print("List Latt element at indext -1:", data[-1])
#List slice
print("List elemets in range 0(inclusive) to 5(Exclusive)", data[0:5])
print("List elemets in range -5(inclusive) to -1(Exclusive)", data[-5:-1])

for num in data:
    print(num, end=' ')
print()

total = 0
for num in data:
    total += num
print('The sum of \'data\' is:', total)

#Another way to sum
total_2 = sum(data)
print('The sum of \'data\' with Pyhon sum():', total_2)

find_max = data[0]
for num in data:
    if num > find_max:
        find_max = num
print("Max value is:" , find_max)

find_max_2 = max(data)
print("Max value with Pyhon max():" , find_max_2)


a_new_list = [1, 11, 21, 31, 41, 51]
for i in range(len(a_new_list)):
    print(a_new_list[i], end=' ')
print()


#Buuble sort
data_copy = data[:]
print("Before sort:", data_copy)
for i in range(len(data_copy)):
    for j in range(0, len(data_copy)-i-1):
        if data_copy[j] > data_copy[j+1]:
            data_copy[j], data_copy[j+1] = data_copy[j+1], data_copy[j]
print("After bubble sort:", data_copy)

print("Sort list with Pyhon sorted()", sorted(data))
print()

#List's Methods

a_second_list = [34, 76, 58]
print("a_second_list: ", a_second_list)

a_second_list.append(100)
print("a_second_list after append 100: ", a_second_list)

a_second_list.remove(34)
print("a_second_list after remove 34: ", a_second_list)

a_second_list.reverse()
print("a_second_list reverse: ", a_second_list)


a_second_list.extend([10, 20, 30])
print("a_second_list after extend with list [10, 20, 30]: ", a_second_list)

#Find the index of a value
print("a_second_list index of 20: ", a_second_list.index(20))
#It will crash if value is not there
#print("a_second_list index of 1000: ", a_second_list.index(1000))

##While Loop
n = 10
while n > 0:
    print(n)
    n -= 1

user_input = int(input('Please enter age of class memmber. Type 0 to stop :>>> '))
ages = []
while user_input > 0:
    ages.append(user_input)
    user_input = int(input("The next age :>>> "))
print("You entered all ages are", ages)

print()
count = 0
class_names = []
name = input("Please enter name: To stop just hit Enter ⏎ :>>> ")
while len(name) > 0:
    count += 1
    class_names.append(name)
    print(f'{name} has been added.')
    name = input("next name: To stop just hit Enter ⏎ :>>> ")
print(f'There are {count} people in the class, they are {class_names} ')


#Modulus %
print("Modulus 10%2 = ", 10 % 2)
print("Modulus 10%4 = ", 10 % 4)


##FizzBuzz
n = 101
for i in range(n):
    if i % 5 == 0 and i % 3 == 0:
        print(i, 'Fizzbuzz!!!')
    elif i % 5 == 0:
        print(i, "Buzz")
    elif i % 3 == 0:
        print(i, "Fizz")
    else:
        print(i)

## Create list from range 
print(list(range(10)))
print(list(range(0, 100, 4)))
print(type(range(10)))