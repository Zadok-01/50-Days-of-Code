# Challenge 04

def only_floats(a, b):
    return sum(type(x) == float for x in (a, b))

'''
# But I think this is beter
def only_floats(*a):
    return sum(type(x) == float for x in a)
'''


print(only_floats(12.1, 23))   # 1
print(only_floats(12.1, 2.3))  # 2
print(only_floats(121, 23))    # 0



print('------')

# Challenge 04  --  Extra

def word_index(strings):
    longest = max(strings, key=len)
    ix = strings.index(longest)
    strings.remove(longest)
    second = max(strings, key=len)
    if len(longest) == len(second):
        return 0
    else:
        return ix


words1 = ['Hate', 'remorse', 'vengeance']  # 2
words2 = ['Love', 'Hate']                  # 0

print(word_index(words1))  # 2
print(word_index(words2))  # 0



'''
Challenge #4:

Day 4: Only Floats

Write a function called only_floats, which takes two parameters a and b, and 
returns 2 if both arguments are floats, returns 1 if only one argument is a 
float, and returns 0 if neither argument is a float. If you pass (12.1, 23) 
as an argument, your function should return a 1.

Extra Challenge: Index of the Longest Word

Write a function called word_index that takes one argument, a list of strings 
and returns the index of the longest word in the list. If there is no longest 
word (if all the strings are of the same length), the function should return 
zero (0). For example, the list below should return 2.

words1 = ["Hate", "remorse", "vengeance"] And this list below, shoul return 
zero (0) words2 = ["Love", "Hate"]
'''

