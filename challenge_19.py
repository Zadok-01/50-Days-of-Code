# Challenge 19


def count_words(s):
    return len(s.split())


def count_elements(s):
    whitespaces = sum(ch.isspace() for ch in s)
    return len(s) - whitespaces



data = 'I love learning'
print(count_words(data))  # 3
print(count_elements(data))  # 13



'''
Challenge #19:

Day 19: Words and Elements

Write two functions. The first function is called count_words which takes a 
string of words and counts how many words are in the string.

The second function called count_elements takes a string of words and counts 
how many elements are in the string. Do not count the whitespaces. The first 
function will return the number of words in a string and the second one will 
return the number of elements (less whitespace). If you pass ‘I love learning’, 
the count_words function should return 3 words and count_elements should 
return 13 elements.
'''

