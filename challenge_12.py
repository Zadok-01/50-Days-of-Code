# Challenge 12

def count_dots(s):
    return s.count('.')


data = 'h.e.l.p.'
print(count_dots(data))  # 4
data = 'he.lp.'
print(count_dots(data))  # 2



print('------')

# Challenge 12  --  Extra

from datetime import date
from calendar import leapdays


def is_valid(yob):
    if len(yob) != 4:
        return False
    
    try:
        yob = int(yob)
    except ValueError:
        return False
    
    if int(yob) < 1900:
        return False
    
    return True


def age_in_minutes():
    yob = input('Enter year of birth: ')
    
    while not is_valid(yob):
        yob = input('Try again.  (Must be four digits after 1900): ')
    
    yob = int(yob)
    current = date.today().year
    days = (current - yob) * 365
    leaps = leapdays(yob, current)
    age_in_mins = (days + leaps) * 24 * 60
    
    print(f'You are {age_in_mins:,} minutes old.')


age_in_minutes()  # 1930 --> 48,388,320



'''
Challenge #12:

Day 12: Count the Dots

Write a function called count_dots. This function takes a string separated by 
dots as a parameter and counts how many dots are in the string. For example, 
‘h.e.l.p.’ should return 4 dots, and ‘he.lp.’ should return 2 dots.

Extra Challenge: Your Age in Minutes

Write a function called age_in_minutes that tells a user how old they are in 
minutes. Your code should ask the user to enter their year of birth, and it 
should return their age in minutes (by subtracting their year of birth to the 
current year). Here are things to look out for:

The user can only input a 4-digit year of birth. For example, 1930 is a valid 
year. However, entering any number longer or less than 4 digits long should 
render input invalid. Notify the user to input a four digits number.

AMENDMENT 1:

If a user enters a year before 1900, your code should tell the user that 
input is invalid. If the user enters the year 

The code should run until the user inputs a valid year. Your function should 
return the user's age in minutes. For example:
If you enter 1930 you are 48,355,200 minutes old.
(NB:  EXAMPLE NO LONGER VALID)

AMMENDMENT 2:

Account for leap years as well.
'''

