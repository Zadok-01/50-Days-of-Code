# Challenge 28


def index_position(s):
    return [ix for ix, ch in enumerate(s) if ch.islower()]


txt = 'LovE'
print(index_position(txt))  # [1,2]



print('------')

# Challenge 28  --  Extra


def largest_number(nums):
    digits = sum((list(str(num)) for num in nums), [])
    big_num = int(''.join(sorted(digits, reverse=True)))
    return f'{big_num:,}'


list1 = [3, 67, 87, 9, 2]
print(largest_number(list1))  # 9,877,632



'''
Challenge #28:

Day 28: Return Indexes

Write a function called index_position. This function takes a string as a 
parameter and returns the positions or indexes of all lower letters in the 
string. For example, ‘LovE’ should return [1,2].

Extra Challenge: Largest Number

Write a function called largest_number that takes a list of integers and 
re-arrange the individual digits to create the largest number possible. For 
example, if you pass the following as an argument: list1 = [3, 67, 87, 9, 2]. 
Your code should return the number in this exact format: 9,877,632 as the 
largest number.
'''

