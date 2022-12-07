# Challenge 01

def divide_or_square(num):
    return num % 5 if num % 5 else num ** .5


print(divide_or_square(10))
print(divide_or_square(13))



print('------')

# Challenge 01  --  Extra

def longest_value(d):
    return max(d.values(), key=len)


fruits = {'fruit': 'apple', 'color': 'green'}
print(longest_value(fruits))



'''
Challenge #1:

Day 1: Division and Square-root

Write a function called divide_or_square that takes one argument (a number), 
and returns the square root of the number if it is divisible by 5, returns 
its remainder if it is not divisible by 5. For example, if you pass 10 as 
an argument, then your function should return 3.16 as the square root.


Extra Challenge: Longest Value

Write a function called longest_value that takes a dictionary as an argument 
and returns the first longest value of the dictionary. For example, the 
following dictionary should return – apple as the longest value.

fruits = {'fruit': 'apple', 'color': 'green'}
'''

