# Challenge 48


# Solution 1 - Using Python's bisect modudule

from bisect import bisect_left


def search_binary_1(data, target):
    ix = bisect_left(data, target)
    if ix < len(data) and data[ix] == target:
        return ix
    return None


data = [12, 13, 22, 34, 45, 56, 78, 98]
target = 22
print(search_binary_1(data, target))  # 2
target = 36
print(search_binary_1(data, target))  # None



print('------')

# Solution 2 - Recursive

def search_binary_2(data, target):
    if len(data) == 1 and data[0] != target:
        return False
    lower, upper = 0, len(data)
    mid_ix = (lower + upper) // 2
    mid_val = data[mid_ix]
    if mid_val == target:
        return mid_ix
    if mid_val < target:
        rv = search_binary_2(data[mid_ix:], target)
        return mid_ix + rv if rv else rv
    rv = search_binary_2(data[:mid_ix], target)
    return lower + rv if rv else rv


data = [12, 13, 22, 34, 45, 56, 78, 98]
target = 22
print(search_binary_2(data, target))  # 2
target = 36
print(search_binary_2(data, target))  # False



print('------')

# Solution 3 - Iterative

def search_binary_3(data, target):
    lower, upper = 0, len(data)
    while lower < upper:
        mid_ix = (lower + upper) // 2
        mid_val = data[mid_ix]
        if mid_val < target:
            lower = mid_ix + 1
        else:
            upper = mid_ix
    if lower < len(data) and data[lower] == target:
        return lower
    return None


data = [12, 13, 22, 34, 45, 56, 78, 98]
target = 22
print(search_binary_3(data, target))  # 2
target = 36
print(search_binary_3(data, target))  # None



'''
Challenge #48:

Day 48: Binary Search

Write a function called search_binary that searches for the number 22 in 
the following list and returns its index. The function should take two 
parameters, the list and the item that is being searched for. Use binary 
search (iterative Method).

list1 = [12, 34, 56, 78, 98, 22, 45, 13]
'''

