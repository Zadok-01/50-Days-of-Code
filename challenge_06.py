# Challenge 06

def user_name(email):
    return email.split('@')[0]


email = 'ben@gmail.com'
print(user_name(email))  # ben



print('------')

# Challenge 06  --  Extra

def zeroed(nums):
    nums[0] = nums[-1] = 0
    return nums


nums = [2, 5, 7, 8, 9]
print(zeroed(nums))  # [0, 5, 7, 8, 0]



'''
Challenge #6:

Day 6: User Name Generator

Write a function called user_name that generates a username from the user’s 
email. The code should ask the user to input an email and the code should 
return everything before the @ sign as their user name. For example, 
if someone enters ben@gmail.com, the code should return ben as their 
user name.

Extra Challenge: Zero Both Ends

Write a function called zeroed code that takes a list of numbers as an 
argument. The code should zero (0) the first and the last number in the list. 
For example, if the input is [2, 5, 7, 8, 9], 
your code should return [0, 5, 7, 8, 0].

'''

