# Challenge 31


def longest_word(words):
    longest = max(words, key=len)
    return [len(longest), longest]


words = ['Java', 'JavaScript', 'Python']
print(longest_word(words))  # [10, JavaScript]



print('------')

# Challenge 31  --  Extra


pwd_dict = {}


def create_user():
    un = input('Enter name: ')
    age = int(input('Enter age: '))
    pw = input('Enter password: ')
    
    pwd_dict[un] = (age, pw)
    print('User saved.  Please login.')
    
    while True:
        un = input('Enter name: ')
        pw = input('Enter password: ')
        stored = pwd_dict.get(un)
        if stored:
            _, stored_pw = stored
            if pw == stored_pw:
                print('Logged in successfully.')
                break
        print('Wrong Pass or User')


create_user()



'''
Challenge #31:

Day 31: Longest Word

Write a function that has one parameter and takes a list of words as an 
argument. The function returns the longest word from the list. Name the 
function longest_word. The function should return the longest word and the 
number of letters in that word. For example, if you pass 
[‘Java, ‘JavaScript’, ‘Python’], your function should return 
[10, JavaScript]


Extra Challenge: Create User

Write a function called create_user. This function asks the user to enter 
their name, age, and password and saves it in a dictionary.

Once the information is saved. The function should print to the user 
that - "User saved. Please login"

The function should then ask the user to re-enter their name and password. 
If the name and password match, the function should return 
"Logged in successfully". If the name and password do not match, the 
function should print 'Wrong Pass or User'. The function should keep 
running until the user enters correct logging details.
'''

