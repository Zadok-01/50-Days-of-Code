# Challenge 16

def sum_list(nested):
    return sum(_flatten(nested))


def _flatten(seq):
    for el in seq:
        if type(el) == list:
            yield from _flatten(el)
        else:
            yield el


nested = [[2, 4, 5, 6], [2, 3, 5, 6]]
print(sum_list(nested))  # 33



print('------')

# Challenge 16  --  Extra


def unique(nested):
	d = dict.fromkeys(_flatten(nested))
	return [*d.keys()]


nested = [[12, 34, 56, 67], [34, 68, 78]]
print(unique(nested))  # [12, 34, 56, 67, 68, 78]



'''
Challenge #16:

Day 16: Sum the List

Write a function called sum_list with one parameter that takes a nested list 
of integers as an argument and returns the sum of the integers. For example, 
if you pass [[2, 4, 5, 6], [2, 3, 5, 6]] as an argument your function should 
return a sum of 33.

Extra Challenge: Unpack A Nest

Nested_list = [[12, 34, 56, 67], [34, 68, 78]]
Write a code that generates a list of the following numbers from the nested 
list above – 34, 67, 78. Your output should be another list: [34, 67, 78]. 
The list output should not have duplicates.
'''

