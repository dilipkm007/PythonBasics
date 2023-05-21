#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 21:21:10 2023

@author: Dilip kumar
"""

list_1 = [1, 2, 3, 4, 5]
list_2 = ['a', 'b', 'c', 'd', 'e']
joined = list(zip(list_1, list_2))
print("joined", joined, "type", type(joined))
print()
i, j = zip(*joined)
print('i=', i, '\tj=', j)


#Moremethod on string
jamesclear = '''
The ultimate productivity hack is saying no. Not doing something will always be faster than doing it. This statement reminds me of the old computer programming saying, “Remember that there is no code faster than no code.” The same philosophy applies in other areas of life. For example, there is no meeting that goes faster than not having a meeting at all. This is not to say you should never attend another meeting, but the truth is that we say yes to many things we don’t actually want to do. There are many meetings held that don’t need to be held. There is a lot of code written that could be deleted.

'''

new_words = jamesclear.split(' ')
for i in range(len(new_words)):
    new_words[i] = new_words[i].strip('\n')
print(new_words)
print('goal' in new_words)
print('meeting' in new_words)

##Tuple
my_tuple = (1, 2, 3, 4)
my_list = [1, 2, 3, 4]
my_string = 'India'

print(my_tuple[0])
print(my_tuple[:3])

my_list[0] = 1000
print(my_list)
#my_tuple[0] = 2000 will get error imutable
print(my_tuple)
#my_string[0] = 'I' will get error imutable
print(my_string) 
