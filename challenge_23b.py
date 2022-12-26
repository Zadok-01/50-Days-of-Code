# Challenge 23


from itertools import chain, repeat
from operator import add, sub, mul, truediv


ops = '+-*/'
funcs = add, sub, mul, truediv
operations = dict(zip(ops, funcs))


def simple_calculator():
    while True:
        prompt = 'Enter first operand (numeric value), or "Q" to quit: '
        validator = validate_numer1
        operand1 = get_user_input(validator, prompt)
        if isquit(operand1):
            break
        
        prompt = 'Enter operator (+ - * /): '
        validator = validate_oper
        operator = get_user_input(validator, prompt)
        
        prompt = 'Enter second operand (numeric value): '
        validator = validate_numer2
        operand2 = get_user_input(validator, prompt)
        
        result = evaluate(operator, float(operand1), float(operand2))
        if result:
            if result.is_integer():
                result = int(result)
            print(result)
        print()


def get_user_input(validator, prompt1, prompt2='Try again: '):
    prompts = chain([prompt1], repeat(prompt2))
    user_entry = map(input, prompts)
    return next(filter(validator, user_entry))


def validate_numer1(entry):
    try:
        float(entry)
        return True
    except ValueError:
        if isquit(entry):
            return True
        return False


def validate_numer2(entry):
    try:
        float(entry)
        return True
    except ValueError:
        return False


def validate_oper(entry):
    ##return entry in '+-*/'
    return entry in ops


def isquit(entry):
    return entry.strip()[0].upper() == 'Q'


def evaluate(op, x, y):
    try:
        return operations[op](x, y)
    except ZeroDivisionError:
        print('Error, division by zero.')
        return None


simple_calculator()



print('------')

# Challenge 23  --  Extra


from math import prod


def multiply_words(s):
    return prod(len(wd) for wd in s.split() if wd.islower())


text = 'love live and laugh'
print(multiply_words(text))  # 240

text = 'Hate war love Peace'
print(multiply_words(text))  # 12



'''
Challenge #23:

Day 23: Simple Calculator

Create a simple calculator. The calculator should be able to perform basic math 
operations, add, subtract, divide and multiply. The calculator should take input 
from users. The calculator should be able to handle ZeroDivisionError, NameError, 
and ValueError.

Extra Challenge: Multiply Words

s = "love live and laugh"
Write a function called multiply_words that takes a string as an argument and 
multiplies the length of each word in the string by the length of other words in 
the string. For example, the string above should return 240 - love (4) live (4) 
and (3) laugh (5). However, your function should only multiply words will all 
lowercase letters. If a word has one upper case letter, it should be ignored. 
For example, the following string:
s = "Hate war love Peace" should return 12 – war (3) love (4). Hate and Peace 
will be ignored because they have at least one uppercase letter.
'''

