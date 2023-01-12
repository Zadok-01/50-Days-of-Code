# Challenge 40


def translate(s):
    words = s.lower().split()
    pig =[]
    vowels = 'aeiou'
    for word in words:
        first = word[0]
        if first in vowels:
            word += 'yay'
        else:
            word = word[1:] + first + 'ay'
        pig.append(word)
    return ' '.join(pig)


txt = 'i love python'
print(translate(txt))  # 'iyay ovelay ythonpay'



'''
Challenge #40:

Day 40: Pig Latin

Write a function called translate that takes the following words and 
translates them into pig Latin.

a = 'i love python'

Here are the rules:

If a word starts with a vowel (a, e, i, o, u) add ‘yay’ at the end. 
For example, ‘eat’ will become ‘eatyay’

If a word starts with anything other than a vowel, move the first letter to 
the end and add ‘ay’ to the end. For example, ‘day’ will become ‘ayday’.

Your code should return:

iyay ovelay ythonpay
'''

