# Challenge 11

def equal_strings(s1, s2):
    return sorted(s1) == sorted(s2)


word1 = 'love'
word2 = 'evol'
print(equal_strings(word1, word2))  # True



print('------')

# Challenge 11  --  Extra

def swap_values(nums):
    nums[0], nums[-1] = nums[-1], nums[0]
    return nums


nums = [2, 4, 67, 7]
print(swap_values(nums))  # [7, 4, 67, 2]



'''
Challenge #11:

Day 11: Are They Equal?

Write a function called equal_strings. The function takes two strings as 
arguments and compares them. If the strings are equal (if they have the same 
characters and have equal length), it should return True, if they are not, 
it should return False. For example, ‘love’ and ‘evol’ should return True.

Extra Challenge: Swap Values

Write a function called swap_values. This function takes a list of numbers 
and swaps the first element with the last element. For example, if you 
pass [2, 4,67, 7] as a parameter, your function should return [7, 4, 67, 2].
'''

