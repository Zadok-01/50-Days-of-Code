# Challenge 21


def make_tuples(a, b):
    return [*zip(a, b)]


a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
print(make_tuples(a, b))  # [(1,5), (2,6), (3,7), (4,8)]



print('------')

# Challenge 21  --  Extra


def even_or_average(*args):
    evens = [arg for arg in args if not arg & 1]
    if evens:
        return max(evens)
    else:
        return sum(args) / 5


a, b, c, d, e = 1, 2, 3, 4 ,5
print(even_or_average(a, b, c, d, e))  # 4

a, b, c, d, e = 1 ,3 ,5, 7, 9
print(even_or_average(a, b, c, d, e))  # 5.0



'''
Challenge #21:

Day 21: List of Tuples

Write a function called make_tuples that takes two lists, equal lists, and 
combines them into a list of tuples. For example, if list a is [1,2,3,4] and 
list b is [5,6,7,8], your function should return [(1,5), (2,6), (3,7), (4,8)].

Extra Challenge: Even Number or Average

Write a function called even_or_average that ask a user to input five numbers. 
Once the user is done, the code should return the largest even number in the 
inputted numbers. If there is no even number in the list, the code should 
return the average of all the five numbers.

AMENDMENT:

Data provided outside the function.
'''

