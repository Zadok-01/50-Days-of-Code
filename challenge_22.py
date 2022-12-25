# Challenge 22


def add_hash(s):
    return s.replace(' ', '#')


def add_underscore(s):
    return s.replace('#', '_')


def remove_underscore(s):
    return s.replace('_', ' ')


print(remove_underscore(add_underscore(add_hash('Python'))))  # 'Python'
print(remove_underscore(add_underscore(add_hash('aaa bbb ccc'))))  # 'aaa bbb ccc'



'''
Challenge #22:

Day 22: Add Under_Score

Create three functions. The first called add_hash takes a string and adds a 
hash # between the words. The second function called add_underscore removes 
the hash (#) and replaces it with an underscore "_".  The third function 
called remove_underscore, removes the underscore and replaces it with nothing. 
If you pass 'Python' as an argument for the three functions, and you call them 
at the same time like: print(remove_underscore(add_underscore(add_hash('Python'))))
it should return 'Python'.
'''

