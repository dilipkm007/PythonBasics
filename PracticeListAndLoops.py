#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 06:04:46 2023

@author: Dilip Kumar
"""
print()
print("#1")
#Problem: 1
'''
    Take Two numbers input from user between 1 and 10. The count
    from lower number to higher number . Print result in screen
'''
num1 = int(input("Please enter a number between 1-100 :👉 "))
num2 = int(input("Please enter a number between 1-100 :👉 "))

while num1 < 1 or num2 < 1 or num1 > 100 or num2 > 100 or num1 == num2:
    print("❌ Numbes must be different values between 1 and 100 Try again! 👍")
    num1 = int(input("Please enter a number between 1-100 :👉 "))
    num2 = int(input("Please enter a number between 1-100 :👉 "))
if num1 > num2:
    for i in range(num2, num1+1):
        print(i, end=' ')
else:
    for i in range(num1, num2+1):
        print(i, end=' ')

print()
print()

print()
print("#2")
#Problem: 2
'''
    Take string input from user
    and print it in reverse order. (use for loop)
'''
name = input("Please enter the string you want to reverse :👉 ")
reverse_String = ''
for char in name:
    reverse_String = char + reverse_String
print(reverse_String)
    
#anotherway
print(name[::-1])


print()
print("#3")
#Problem: 3
'''
    Ask user to input number between 1 and 12
    and print table of that number
'''

strNum = input("Pelase enter number between 1-12 i will show you table :👆")
while (not strNum.isdigit()) or  int(strNum) <  1 or int(strNum) > 12:
    strNum = input("Try Again! Pelase enter number between 1-12 i will show you table :👆")
num = int(strNum)
for i in range(1, 11):
    print(f'{i} x {num} = {i * num}')
print()



print()
print("#4")
#Problem: 4
'''
    print all 1 to 12 tables
'''

for i in range(1, 13):
    print("============================================================")
    print()
    print(f'This is the {i}\'s times table')
    print()
    for j in range(1, 11):
        print(f'{j} x {i} = {j * i}')
    print("============================================================")
    print()


print()
print("#5")
#Problem: 5
'''
    Input list of numbers from user and calculate mean
'''

aNum = input("Please enter number (To exit 'Enter ⏎') :👉 ")
numbers = []
while len(aNum) > 0:
    while not aNum.isdigit():
        print("❌ please enter number only ")
        aNum = input("😊 Try again! Please enter number To exite 'Enter ⏎' :👉 ")
    numbers.append(int(aNum))
    aNum = input("Please enter another (To exit 'Enter ⏎') :👉 ")
total = 0
for num in numbers:
    total += num
print(f"The Mean of {numbers} is {total/len(numbers)}")



print()
print("#6")
#Problem: 6
'''
    Take input from user and calculate factorial of that number
'''

numStr = input("Please provide a number to factorial: 👉")
while not numStr.isdigit():
   print("❌ its not a number please try again 🔦")
   numStr = input("Try Again!! Please provide a number to factorial: 👉")

num = int(numStr)
fact = 1
while num != 1:
    fact = fact * num
    num = num - 1
print("So here is your answer :🍎:", fact)



print()
print("#7")
#Problem: 7
'''
   calculate the fibonacci seriece upto users input
'''

numStr = input("Please enter number upto you want fibonacci series: 🤯 ")
while not numStr.isdigit():
    print("❌ its not a number please try again 🔦")
    numStr = input("Try Again!! Please enter number upto you want fibonacci series: 🤯 ")
n = int(numStr)
a = 0
b = 1
fibonacci = []
for i in range(n):
    fibonacci.append(a)
    a,b = b, a+b


print(f"The first {n} Fibonacci numbers are {fibonacci}")






print()
print("#9")
#Problem: 9
'''
 print *s
 *****
 *
 *****
 *
 *
 *
'''


star = '*'
for i in range(1,7):
    for j in range(1, 6):
        if (i == 1 or i == 3) and j < 6:
            print(star, end='')
        elif j == 1:
            print(star, end='')
    print()


print()
print("#10")
#Problem: 10
'''
from 1 to 100 number create two list odd and even an print it
'''
n = 100
odds =[]
evens = []
for i in range(n+1):
    if i % 2 == 0:
        evens.append(i)
    else:
        odds.append(i)

print(f'The evens are ✌️ {evens}')
print(f'The odds are ☝️ {odds}')


