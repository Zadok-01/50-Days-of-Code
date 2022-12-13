# Challenge 10

def hide_password(pwd):
    size = len(pwd)
    return '*' * size, size


pwd = 'hello'
print(hide_password(pwd))  # ('*****', 5)



print('------')

# Challenge 10  --  Extra

def convert_numbers(nums):
    return [f'{n:,}' for n in nums]


pwd = nums = [1000000, 2356989, 2354672, 9878098]
print(convert_numbers(nums))
# ['1,000,000', '2,356,989', '2,354,672', '9,878,098']



'''
Challenge #10:

Day 10: Hide my Password

Write a function called hide_password that takes one parameter. The function 
takes a a password from a user and returns a hidden password. For example, 
if the user enters ‘hello’ as a password the function should return
‘*****’
as a password and tell the user that the password is 5 characters long.

Extra Challenge: A Thousand Separator

Your new company has a list of figures saved in a list. The issue is that 
these numbers have no separator. The numbers are saved in the following 
format: [1000000, 2356989, 2354672, 9878098].

You have been asked to write a code that will convert each of the numbers 
in the list into a string. Your code should then add a comma on each number 
as a thousand separator for readability. When you run your code on the above 
list, your output should be:

[ '1,000,000', '2,356,989', '2,354,672', '9,878,098’]

Write a function called convert_numbers that will take one argument, a list 
of numbers above.
'''

