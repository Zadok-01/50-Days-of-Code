# Challenge 15

def same_in_reverse(s):
    return s == s[::-1]


word = 'dad'
print(same_in_reverse(word))  # True



print('------')

# Challenge 15  --  Extra


def your_age(name):
    name = name.lower()
    age = names_age.get(name)
    if age is None:
        print('Your age is not in the database.')
        age = int(input('What is your age? '))
        names_age[name] = age
    name = name.capitalize()
    return f'Hi, {name}, you are {age} years old.'


names_age = {'jane': 23, 'kerry': 45, 'tim': 34, 'peter': 27}

name = 'Peter'
print(your_age(name))  # Hi, Peter, you are 27 years old.

name = 'Eric'  # say 37
print(your_age(name))  # Hi, Eric, you are 37 years old.



'''
Challenge #15:

Day 15: Same in Reverse

Write a function called same_in_reverse that takes a string and checks if 
the string reads the same in reverse.
If it is the same, the code should return True.
If not, it should return False.
For example, ‘dad’ should return True, because it reads the same in reverse.

Extra Challenge: What’s My Age?

Write a function called your_age. This function should take a name and then 
it return their age. For example, if 'Peter' is passed, your function should 
return, ‘Hi, Peter, you are 27 years old.

This function reads data from the 'database' (dictionary below). If the name 
is not in the dictionary, your code should tell the user that their name is 
not in the dictionary, and ask them for their age. Your code should then add 
the name and age to the dictionary of names_age below. Once added your code 
should return to the user ‘Hi, (added name), you are (added age) years old’. 
Only lowercase names should be stored.

names_age = {"jane": 23, "kerry": 45, "tim": 34, “peter": 27}
'''

