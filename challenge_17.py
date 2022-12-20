# Challenge 17


from random import randint


def user_name(name):
    return name[::-1] + str(randint(0, 9))


name = 'Fred'
print(user_name(name))  # Example:  derF3



print('------')

# Challenge 17  --  Extra


def sort_by_length(names):
    # built-in sort functions prohibited
    out = []
    while names:
        ix = names.index(min(names, key=len))
        out.append(names.pop(ix))
    return out


names = ['Peter', 'Jon', 'Andrew']
print(sort_by_length(names))  # ['Jon', 'Peter', 'Andrew']



'''
Challenge #17:

Day 17: User Name Generator

Write a function called user_name, that creates a username for the user. 
The function should ask a user to input their name. The function should then 
reverse the name and attach a randomly issued number between 0 – 9 at the 
end of the name. The function should return the username.

AMENDMENT:

Personally, I think it's fine if you just pass a list into an argument, and 
it outputs. Input is overrated.

Extra Challenge: Sort by Length

names = [ "Peter", "Jon", "Andrew"]

Write a function called sort_length that takes a list of strings as an 
argument, and sorts the strings in ascending order according to their length. 
For example, the list above should return:
['Jon', 'Peter', 'Andrew']
Do not use the built-in sort functions
'''

