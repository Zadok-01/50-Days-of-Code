# Challenge 24


def average_calories():
    cals = 0
    count = 1
    while True:
        intake = input(f'Enter calorie intake for day {count} or X to terminate: ')
        if 'X' in intake.upper():
            break
        else:
            cals += float(intake)
            count += 1
    return cals / (count - 1)


print(average_calories())



print('------')

# Challenge 24  --  Extra


def nested_lists(*args):
    return [*args]


seq1 = [1, 2, 3, 5]
seq2 = [1, 2, 3, 4]
seq3 = [1, 3, 4, 5]

print(nested_lists(seq1, seq2, seq3))
# [[1, 2, 3, 5], [1, 2, 3, 4], [1, 3, 4, 5]]



'''
Challenge #24:

Day 24: Average Calories

Create a function called average_calories that calculates the average calories 
intake of a user. The function should ask the user to input their calories intake 
for any number of days and once they hit ‘done’ it should calculate and return 
    the average intake.

Extra Challenge: Create a Nested List

Write a function called nested_lists that takes any number of lists and creates 
a 2-dimensional nested list of lists. For example, if you pass the following 
lists as arguments: [1, 2, 3, 5], [1, 2, 3,4], [1, 3, 4, 5].
Your code should return: [[1, 2, 3, 5], [1, 2, 3, 4], [1, 3, 4, 5]]
'''

