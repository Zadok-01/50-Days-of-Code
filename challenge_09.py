# Challenge 09

def biggest_odd(digits):
    digits = map(int, digits)
    return max((d for d in digits if d & 1), default=None)


digits = '23569'
print(biggest_odd(digits))  # 9



print('------')

# Challenge 09  --  Extra

def zeros_last(nums):
    zeros = nums.count(0)
    if not zeros:
        return sorted(nums)
    else:
        nums = filter(None, nums)
        return [*nums] + [0] * zeros


data = [1, 4, 6, 0, 7,0,9]
print(zeros_last(data))  # [1, 4, 6, 7, 9, 0, 0]

data = [2, 1, 4, 7, 6]
print(zeros_last(data))  # [1, 2, 4, 6, 7]



'''
Challenge #9:

Day 9: Biggest Odd Number

Create a function called biggest_odd that takes a string of numbers and 
returns the biggest odd number in the list. For example, if you pass ‘23569’ 
as an argument, your function should return 9. Use list comprehension.

Extra Challenge: Zeros to the End

Write a function called zeros_last. This function takes a list as argument. 
If a list has zeros (0), it will move them to the front of the list and 
maintain the order of the other numbers in the list. If there are no Zeros 
in the list, the function should return the original list sorted in ascending 
order. For example, if you pass [1, 4, 6, 0, 7,0,9] as an argument, your 
code should return [1, 4, 6, 7, 9, 0, 0]. If you pass [2, 1, 4, 7, 6] as 
your argument, your code should return [1, 2, 4, 6, 7].
'''

