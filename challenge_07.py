# Challenge 07

def string_range(x):
    return '.'.join(map(str, range(x)))


x = 6
print(string_range(x))  # '0.1.2.3.4.5'



print('------')

# Challenge 07  --  Extra

def names_with_s(names):
    return {n: names.count(n) for n in names if n.startswith('S') }


names = ['Joseph', 'Nathan', 'Sasha', 'Kelly', 'Muhammad', 'Jabulani', 'Sera', 'Patel', 'Sera']
print(names_with_s(names))  # {'Sasha': 1, 'Sera': 2}



'''
Challenge #7:

Day 7: A String Range

Write a function called string_range that takes a single number and returns 
a string of its range. The string characters should be separated by dots(.)
For example, if you pass 6 as an argument, your function should return 
‘0.1.2.3.4.5’.

Extra Challenge: Dictionary of Names

You are given a list of names, and you are asked to write a code that 
returns all the names that start with ‘S’. Your code should return a 
dictionary of all the names that start with S and how many times they appear 
in the dictionary. Here is a list below:

names = ["Joseph","Nathan", "Sasha", "Kelly", "Muhammad", "Jabulani", 
"Sera”, "Patel", "Sera”]

Your code should return: {“Sasha”: 1, “Sera”: 2}
'''

