#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 22:20:06 2023

@author: Dilip Kumar
"""

##Dictionary
flags = {'india': '🇮🇳', 'japan': '🇯🇵', 'usa': '🇺🇸', 'france':'🇫🇷', 'russia': '🇷🇺'}
print(flags['india'])
print(flags.get('japan'))
# print(flags['canada']) #it will crash
print(flags.get('canada')) #it will not crash
flags['germany'] = '🇩🇪'
print(flags)
print("\n")
print(flags.items())

## iterate over Keys
for country in flags:
    print(country)

print()

for country, flag in flags.items():
    print(f'The flag of {country} is {flag}')
    
print()
print(flags.keys())
print()
print(flags.values())

if 'india' in flags:
    print('india is in flags')
else:
    print('india is not in flags')

if 'nepal' in flags:
    print('Nepal is in flags')
else:
    print('nepal is not in flags')
    
    
# same we can check with list
numList = [1, 2, 3, 4, 5, 6]
print("is 2 in numList︖ ", 2 in numList)
print("is 7 in numList ？", 7 in numList)



print()
print()

sherlock = '''
The economist J.K. Galbraith once wrote, “Faced with a choice between changing one’s mind and proving there is no need to do so, almost everyone gets busy with the proof.”

Leo Tolstoy was even bolder: “The most difficult subjects can be explained to the most slow-witted man if he has not formed any idea of them already; but the simplest thing cannot be made clear to the most intelligent man if he is firmly persuaded that he knows already, without a shadow of doubt, what is laid before him.”

What’s going on here? Why don’t facts change our minds? And why would someone continue to believe a false or inaccurate idea anyway? How do such behaviors serve us?
The Logic of False Beliefs
Humans need a reasonably accurate view of the world in order to survive. If your model of reality is wildly different from the actual world, then you struggle to take effective actions each day.

However, truth and accuracy are not the only things that matter to the human mind. Humans also seem to have a deep desire to belong.

In Atomic Habits, I wrote, “Humans are herd animals. We want to fit in, to bond with others, and to earn the respect and approval of our peers. Such inclinations are essential to our survival. For most of our evolutionary history, our ancestors lived in tribes. Becoming separated from the tribe—or worse, being cast out—was a death sentence.”

Understanding the truth of a situation is important, but so is remaining part of a tribe. While these two desires often work well together, they occasionally come into conflict.

In many circumstances, social connection is actually more helpful to your daily life than understanding the truth of a particular fact or idea. The Harvard psychologist Steven Pinker put it this way, “People are embraced or condemned according to their beliefs, so one function of the mind may be to hold beliefs that bring the belief-holder the greatest number of allies, protectors, or disciples, rather than beliefs that are most likely to be true.”

We don’t always believe things because they are correct. Sometimes we believe things because they make us look good to the people we care about.

I thought Kevin Simler put it well when he wrote, “If a brain anticipates that it will be rewarded for adopting a particular belief, it’s perfectly happy to do so, and doesn’t much care where the reward comes from — whether it’s pragmatic (better outcomes resulting from better decisions), social (better treatment from one’s peers), or some mix of the two.”

False beliefs can be useful in a social sense even if they are not useful in a factual sense. For lack of a better phrase, we might call this approach “factually false, but socially accurate.” When we have to choose between the two, people often select friends and family over facts.

This insight not only explains why we might hold our tongue at a dinner party or look the other way when our parents say something offensive, but also reveals a better way to change the minds of others.

Facts Don’t Change Our Minds. Friendship Does.
Convincing someone to change their mind is really the process of convincing them to change their tribe. If they abandon their beliefs, they run the risk of losing social ties. You can’t expect someone to change their mind if you take away their community too. You have to give them somewhere to go. Nobody wants their worldview torn apart if loneliness is the outcome.

The way to change people’s minds is to become friends with them, to integrate them into your tribe, to bring them into your circle. Now, they can change their beliefs without the risk of being abandoned socially.

The British philosopher Alain de Botton suggests that we simply share meals with those who disagree with us:

“Sitting down at a table with a group of strangers has the incomparable and odd benefit of making it a little more difficult to hate them with impunity. Prejudice and ethnic strife feed off abstraction. However, the proximity required by a meal – something about handing dishes around, unfurling napkins at the same moment, even asking a stranger to pass the salt – disrupts our ability to cling to the belief that the outsiders who wear unusual clothes and speak in distinctive accents deserve to be sent home or assaulted. For all the large-scale political solutions which have been proposed to salve ethnic conflict, there are few more effective ways to promote tolerance between suspicious neighbours than to force them to eat supper together.”

Perhaps it is not difference, but distance that breeds tribalism and hostility. As proximity increases, so does understanding. I am reminded of Abraham Lincoln’s quote, “I don’t like that man. I must get to know him better.”

Facts don’t change our minds. Friendship does.

The Spectrum of Beliefs
Years ago, Ben Casnocha mentioned an idea to me that I haven’t been able to shake: The people who are most likely to change our minds are the ones we agree with on 98 percent of topics.

If someone you know, like, and trust believes a radical idea, you are more likely to give it merit, weight, or consideration. You already agree with them in most areas of life. Maybe you should change your mind on this one too. But if someone wildly different than you proposes the same radical idea, well, it’s easy to dismiss them as a crackpot.

One way to visualize this distinction is by mapping beliefs on a spectrum. If you divide this spectrum into 10 units and you find yourself at Position 7, then there is little sense in trying to convince someone at Position 1. The gap is too wide. When you’re at Position 7, your time is better spent connecting with people who are at Positions 6 and 8, gradually pulling them in your direction.

The most heated arguments often occur between people on opposite ends of the spectrum, but the most frequent learning occurs from people who are nearby. The closer you are to someone, the more likely it becomes that the one or two beliefs you don’t share will bleed over into your own mind and shape your thinking. The further away an idea is from your current position, the more likely you are to reject it outright.

When it comes to changing people’s minds, it is very difficult to jump from one side to another. You can’t jump down the spectrum. You have to slide down it.

Any idea that is sufficiently different from your current worldview will feel threatening. And the best place to ponder a threatening idea is in a non-threatening environment. As a result, books are often a better vehicle for transforming beliefs than conversations or debates.

In conversation, people have to carefully consider their status and appearance. They want to save face and avoid looking stupid. When confronted with an uncomfortable set of facts, the tendency is often to double down on their current position rather than publicly admit to being wrong.

Books resolve this tension. With a book, the conversation takes place inside someone’s head and without the risk of being judged by others. It’s easier to be open-minded when you aren’t feeling defensive.

Arguments are like a full frontal attack on a person’s identity. Reading a book is like slipping the seed of an idea into a person’s brain and letting it grow on their own terms. There’s enough wrestling going on in someone’s head when they are overcoming a pre-existing belief. They don’t need to wrestle with you too.

Why False Ideas Persist
There is another reason bad ideas continue to live on, which is that people continue to talk about them.

Silence is death for any idea. An idea that is never spoken or written down dies with the person who conceived it. Ideas can only be remembered when they are repeated. They can only be believed when they are repeated.

I have already pointed out that people repeat ideas to signal they are part of the same social group. But here’s a crucial point most people miss:

People also repeat bad ideas when they complain about them. Before you can criticize an idea, you have to reference that idea. You end up repeating the ideas you’re hoping people will forget—but, of course, people can’t forget them because you keep talking about them. The more you repeat a bad idea, the more likely people are to believe it.

Let’s call this phenomenon Clear’s Law of Recurrence: The number of people who believe an idea is directly proportional to the number of times it has been repeated during the last year—even if the idea is false.

Each time you attack a bad idea, you are feeding the very monster you are trying to destroy. As one Twitter employee wrote, “Every time you retweet or quote tweet someone you’re angry with, it helps them. It disseminates their BS. Hell for the ideas you deplore is silence. Have the discipline to give it to them.”

Your time is better spent championing good ideas than tearing down bad ones. Don’t waste time explaining why bad ideas are bad. You are simply fanning the flame of ignorance and stupidity.

The best thing that can happen to a bad idea is that it is forgotten. The best thing that can happen to a good idea is that it is shared. It makes me think of Tyler Cowen’s quote, “Spend as little time as possible talking about how other people are wrong.”

Feed the good ideas and let bad ideas die of starvation.

The Intellectual Soldier
I know what you might be thinking. “James, are you serious right now? I’m just supposed to let these idiots get away with this?”

Let me be clear. I’m not saying it’s never useful to point out an error or criticize a bad idea. But you have to ask yourself, “What is the goal?”

Why do you want to criticize bad ideas in the first place? Presumably, you want to criticize bad ideas because you think the world would be better off if fewer people believed them. In other words, you think the world would improve if people changed their minds on a few important topics.

If the goal is to actually change minds, then I don’t believe criticizing the other side is the best approach.

Most people argue to win, not to learn. As Julia Galef so aptly puts it: people often act like soldiers rather than scouts. Soldiers are on the intellectual attack, looking to defeat the people who differ from them. Victory is the operative emotion. Scouts, meanwhile, are like intellectual explorers, slowly trying to map the terrain with others. Curiosity is the driving force.

If you want people to adopt your beliefs, you need to act more like a scout and less like a soldier. At the center of this approach is a question Tiago Forte poses beautifully, “Are you willing to not win in order to keep the conversation going?”

Be Kind First, Be Right Later
The brilliant Japanese writer Haruki Murakami once wrote, “Always remember that to argue, and win, is to break down the reality of the person you are arguing against. It is painful to lose your reality, so be kind, even if you are right.”

When we are in the moment, we can easily forget that the goal is to connect with the other side, collaborate with them, befriend them, and integrate them into our tribe. We are so caught up in winning that we forget about connecting. It’s easy to spend your energy labeling people rather than working with them.

The word “kind” originated from the word “kin.” When you are kind to someone it means you are treating them like family. This, I think, is a good method for actually changing someone’s mind. Develop a friendship. Share a meal. Gift a book.

Be kind first, be right later.

'''

#letter count
letter_counts = {}
for letter in sherlock:
    letter_counts[letter.lower()] = letter_counts.get(letter, 0) + 1

letter_count_clean = {}
for k, v in letter_counts.items():
    if k.isalpha():
        letter_count_clean[k] = v

print(letter_count_clean)

import matplotlib.pyplot as plt

x,y = zip(*letter_count_clean.items())
plt.bar(x, y)
plt.show()




















