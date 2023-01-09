# Challenge 37


def count_the_vowels(s):
    #return len(set(ch for ch in s.lower() if ch in 'aeiou'))
    #return len(set(v for v in 'aeiou' if v in s.lower()))
    return sum(v in s.lower() for v in 'aeiou')


txt = 'hello'
print(count_the_vowels(txt))  # 2

txt = 'saas'
print(count_the_vowels(txt))  # 1



'''
Challenge #37:

Day 37: Count the Vowels

Create a function called count_the_vowels. The function takes one argument, 
a string, and returns the number of vowels in the string. For example, 
‘hello’ should return 2 vowels. If a vowel appears in a string more than 
once it should be counted as one. For example, ‘saas’ should return 1 vowel. 
Your code should count lowercase and uppercase vowels.
'''

