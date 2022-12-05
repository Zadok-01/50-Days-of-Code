'''
Challenge #2:
Day 2: Strings to Integers
Write a function called convert_add that takes a list of strings as an argument and converts it to integers and sums the list. For example [‘1’, ‘3’, ‘5’] should be converted to [1, 3, 5] and
summed to 9.

Extra Challenge: Duplicate Names
Write a function called check_duplicates that takes a list of strings as an argument. The function should check if the list has any duplicates. If there are duplicates, the function should return the duplicates. If there are no duplicates, the function should return "No duplicates". For example, the list of fruits below should return apple as a duplicate and list of names should return "no duplicates".
fruits = ['apple', 'orange', 'banana', 'apple']
names = ['Yoda', 'Moses', 'Joshua', 'Mark']
'''

def convert(strings):
    return sum(map(int, strings))

example = ['1', '3', '5']
print(convert(example))


def check_duplicates(strings):
    uniq = set(strings)
    if len(uniq) == len(strings):
        return 'No duplicates'
    else:
        for item in uniq:
            strings.remove(item)
        return list(set(strings))


fruits = ['apple', 'orange', 'banana', 'apple']
fruits2 = ['apple', 'orange', 'banana', 'apple', 'apple', 'apple', 'banana']
names = ['Yoda', 'Moses', 'Joshua', 'Mark']
print(check_duplicates(fruits))
print(check_duplicates(fruits2))
print(check_duplicates(names))

