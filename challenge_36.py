# Challenge 36


####  CLASSICAL  ####

def count(s):
    counts = {}
    for ch in s:
        counts[ch] = counts.setdefault(ch, 0) + 1
    return counts


'''
####  DEFAULTDICT  ####

from collections import defaultdict

def count(s):
    counts = defaultdict(int)
    for ch in s:
        counts[ch] += 1
    return dict(counts)
'''


'''
####  COUNTER  ####

from collections import Counter

def count(s):
    counts = Counter(s)
    return dict(counts)
'''


txt = 'hello'
print(count(txt))  # {'h': 1,'e': 1,'l': 2, 'o': 1}



'''
Challenge #36:
Day 36: Count String
Write a function called count that takes one argument a string, and returns a dictionary of how many times each element appears in the string. For example, ‘hello’ should return:
{‘h’:1,’e’: 1,’l’:2, ‘o’:1}.
'''

