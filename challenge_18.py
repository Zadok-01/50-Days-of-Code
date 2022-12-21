# Challenge 18


def any_number(*args):
    return sum(args) / len(args)



print(any_number(12, 90, 12, 34))  # 37.0
print(any_number(12, 90))  # 51.0

# Could use statistics.mean, but this would convert back to int if possible.



print('------')

# Challenge 18  --  Extra


def add_reverse(seq1, seq2):
    if len(seq1) != len(seq2):
        return 'The lists are not of equal lengths'
    return [a + b for a, b in zip(seq1, seq2)][::-1]


seq1 = [10, 12, 34]
seq2 = [12, 56, 78]
print(add_reverse(seq1, seq2))  # [112, 22, 68]



'''
Challenge #18:

Day 18: Any Number of Arguments

Write a function called any_number that can receive any number of arguments 
(integers and floats) and return the average of those integers. If you pass 
12, 90, 12, 34 as arguments your function should return 37.0 as average. 
If you pass 12, 90 your function should return 51.0 as average.

Extra Challenge: Add and Reverse

Write a function called add_reverse. This function takes two lists as 
argument and adds each corresponding number, and reverses the outcome. 
For example, if you pass [10, 12, 34] and [12, 56, 78]. Your code should 
return [112, 22, 68]. If the two lists are not of equal lengths, the code 
should return a message that "the lists are not of equal lengths".

AMENDMENT:

Result should be [112, 68, 22]
'''

