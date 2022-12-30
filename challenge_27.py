# Challenge 27


def unique_numbers(seq):
    sum_orig = sum(seq)
    uniq = set(seq)
    sum_uniq = sum(uniq)
    diff = sum_orig - sum_uniq
    if diff & 1:
        return [*uniq]
    return seq


nums = [1, 2, 4, 5, 6, 7, 8, 8]
print(unique_numbers(nums))  # [1, 2, 4, 5, 6, 7, 8, 8]



print('------')

# Challenge 27  --  Extra


def difference(seq_a, seq_b):
    pass_1 = [el for el in seq_a if el not in seq_b]
    pass_2 = [el for el in seq_b if el not in seq_a]
    return pass_1 + pass_2


list1 = [1, 2, 4, 5, 6]
list2 = [1, 2, 5, 7, 9]
print(difference(list1, list2))  # [4, 6, 7, 9]



'''
Challenge #27:

Day 27: Unique Numbers

Write a function called unique_numbers that takes a list of numbers as an 
argument. Your function is going to find all the unique numbers in the list. 
It will then sum up the unique numbers. You will calculate the difference 
between the sum of all the numbers in the original list and the sum of 
unique numbers in the list. If the difference is an even number, your 
function should return the original list. If the difference is an odd number, 
your function should return a list with unique numbers only. For example 
[1, 2, 4, 5, 6, 7, 8, 8] should  return [1, 2, 4, 5, 6, 7, 8, 8].

Extra Challenge: Difference of Two Lists

Write a function called difference that takes two lists as arguments. This 
function should return all the elements that are in list A but not in list B 
and all the elements in list B not in list A.

For example:
list1 = [1, 2, 4, 5, 6]
list2 = [1, 2, 5, 7, 9]
should return:
[4, 6, 7, 9]

Use list comprehension in your function.
'''

