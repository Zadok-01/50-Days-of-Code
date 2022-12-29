# Challenge 26


def sort_words(s):
    letters = set(ch for ch in s if not ch.isspace())
    return [','.join(sorted(letters))]


txt = 'love life'
print(sort_words(txt))  # ['e,f,i,l,o,v']



print('------')

# Challenge 26  --  Extra


def string_length(s):
    return {wd: len(wd) for wd in s.split()}


txt = 'Hi my name is Richard'
print(string_length(txt))
# {'Hi': 2, 'my': 2, 'name': 4, 'is': 2, 'Richard': 7}



'''
Challenge #26:

Day 26: Sort Words

Write a function called sort_words that takes a string of words as an 
argument, removes the whitespaces, and returns a list of letters sorted 
in alphabetical order. Letters will be separated by commas. All letters 
should appear once in the list. This means that you sort and remove 
duplicates. For example ‘love life’ should return as ['e,f,i,l,o,v'].

Extra Challenge: Length of Words

s = 'Hi my name is Richard'

Write a function called string_length that takes a string of words (words 
and spaces) as argument. This function should return the length of all the 
words in the string. Return the results in a form of a dictionary. The 
string above should return:

{'Hi': 2, 'my': 2, 'name': 4, 'is': 2, 'Richard': 7}
'''

