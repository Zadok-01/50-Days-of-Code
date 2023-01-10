# Challenge 38


from random import randint


def guess_a_number():
    print('Guess a Number Game\n')
    target = randint(1, 20)
    for i in range(3):
        if i != 0:
            print('Try again.')
        guess = int(input('Guess a number between 1 and 20, inclusive: '))
        if guess < target:
            print('Your guess was too low.')
        elif guess > target:
            print('Your guess was too high.')
        else:
            print('You guessed correctly.\nYou win.')
            return
    print(f'You did not guess correctly.\nThe correct number was {target}.\nYou lose.')


guess_a_number()



print('------')

# Challenge 38  --  Extra


def missing_numbers(seq):
    low = min(seq)
    high = max(seq)
    expected = set(range(low, high+1))
    present = set(seq)
    missing = expected - present
    missing = sorted(missing)
    return missing


data = [1, 2, 3, 5, 6, 7, 9, 11, 12, 23, 14, 15, 17, 18, 19, 20, 21, 22, 
24, 25, 26, 27, 28, 31]
print(missing_numbers(data))  # [4, 8, 10, 13, 16, 29, 30]



'''
Challenge #38:

Day 38: Guess a Number

Write a function called guess_a_number. The function should ask a user to 
guess a randomly generated number. If the user guesses a higher number, 
the code should tell them that the guess is too high, if the user guesses 
low, the code should tell them that their guess is too low. The user should 
get a maximum of three guesses. When the user guesses right, the code 
should declare them a winner. After three wrong guesses, the code should 
declare them a loser.

Extra Challenge: Find Missing Numbers

list = [1, 2, 3, 5, 6, 7, 9, 11, 12, 23, 14, 15, 17, 18, 19, 20, 21, 22, 
24, 25, 26, 27, 28, 31]

Write a function called missing_numbers that takes a list of sequence of 
numbers and finds the missing numbers in the sequence. The list above 
should return:

[4, 8, 10, 13, 16, 29, 30]
'''

