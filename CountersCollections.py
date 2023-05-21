#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 03:33:04 2023

@author: Dilip Kumar
"""

jamesClear = ''' 

One of the central ideas in the book is the concept of building “identity-based habits”, which essentially recommends focusing on the type of person you wish to become rather than the outcome you wish to achieve.

One reader named Roland used the idea to improve his eating habits.

“I stopped eating unhealthy food via identity change,” he wrote. “I tried many times in the past, but it became easy — natural — only after I had made the conscious decision that I want to be someone who eats healthy. Instead of aiming for I want to stop eating bad food, I tried changing the mindset to I am someone that eats healthy and lives a healthy life. It changes how you approach things.”

Another reader named Robert employed this idea to help him quit smoking. He wrote, “I recently stopped smoking and the difference between I don’t smoke and I can’t smoke is a powerful trainer of my brain. The positive message of I don’t smoke is that I have not “given up” anything. I am not sacrificing a pleasure. I am investing in my future happiness and wellbeing.”

Like most strategies in the book, the concept of identity-based habits can be combined with other habit building tactics. For instance, one reader used an external reward of $10 to reinforce the desired identity. “I told myself, I am no longer a drinker. Then, after each day of non-drinking, I gave myself $10 to buy something nice rather than poison (like clothes and household items). Today, I no longer need the allowance and I’m six years sober.”

Chapter 2 of Atomic Habits covers these strategies in much greater detail.

Changing the Cues
Another way you can change a habit is by identifying and altering the cues that prompt your behavior. This is precisely what many readers have done.

One woman named Lisa cultivated a reading habit by increasing her exposure to books. “I’ve read more books by continually having 20-30 books on hold at the library,” she said. “It saves time on browsing for books. I always have new things to read with a three-week deadline.”

Heather used a similar strategy to reinforce the simple habit of drinking more water. “I use color and placement for visual reminding and motivation. I poured water in a bright aqua water bottle – my favorite color – and placed it on my nightstand so I couldn’t miss it when I woke up.”

Other readers have done the opposite. They reduced exposure to negative cues. One man named Max managed to eliminate his e-cigarette habit. “I quit e-cigarettes with a combination of determination and also quitting coffee at the same time, which was a trigger for me as I’d smoke and drink coffee together in the morning.”

'''



from collections import Counter

# print(Counter(jamesClear.lower()))
new_dict = dict(Counter(jamesClear.lower()))
##Dictionary Comprehension
new_dict = {k:v for k, v in new_dict.items() if k.isalpha() or k.isdigit()}
print(new_dict)


##List Comprehension
print()
new_list = [x**2 for x in range(1, 11)]
print(new_list)