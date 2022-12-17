# Challenge 14

def _flatten(seq):
    for el in seq:
        if type(el) == list:
            yield from _flatten(el)
        else:
            yield el


def flat_list(nested):
    return [*_flatten(nested)]


nested = [[2, 4, 5, 6]]
print(flat_list(nested))  # [2, 4, 5, 6]

nested = [[2, [4, [5]], 6]]
print(flat_list(nested))  # [2, 4, 5, 6]



print('------')

# Challenge 14  --  Extra


def your_salary(name, periods, rate):
    basic = periods * rate
    overtime = (periods - 100) * rate / 4
    salary = basic + overtime
    return f'Teacher: {name}, Periods: {periods}\nGross Salary: {salary:,.2f}'


name = input("Enter teacher's name: ")
periods = int(input('Enter number of periods taught: '))
rate = float(input('Enter rate per period: '))

output = your_salary(name, periods, rate)
print(output)
# John Kelly, 105, 20 -->
#
# Teacher: John Kelly, Periods: 105
# Gross Salary: 2,125.00



'''
Challenge #14:

Day 14: Flatten the List

Write a function called flat_list that takes one argument, a nested list. 
The function converts the nested list into a one- dimension list. 
For example [[2,4,5,6]] should return [2,4,5,6].

Extra Challenge: Teacher’s Salary

A school asked you to calculate teachers' salaries. The program should ask 
the user to enter the teacher’s name, the number of periods taught in a 
month, and the rate per period. The monthly salary is calculated by 
multiplying the number of periods by the monthly rate. The current monthly 
rate per period is $20. If a teacher has more than 100 periods in a month, 
everything above 100 is overtime. Overtime is $25 per period. For example, 
if a teacher has taught 105 periods, their monthly gross salary should be 
2,125. Write a function called your_salary that calculates a teacher’s gross 
salary. The function should return the teacher’s name, periods taught, and 
gross salary. Here is how you should format your output:

Teacher: John Kelly, Periods: 105
Gross salary:2,125
'''

