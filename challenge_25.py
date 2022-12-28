# Challenge 25


def all_the_same(arg):
    return len(set(arg)) in (0, 1)


data = ['Mary', 'Mary', 'Mary']
print(all_the_same(data))  # True

data = (5, 5, 5)
print(all_the_same(data))  # True

data = (5, 5, 6)
print(all_the_same(data))  # False

data = 'aaa'
print(all_the_same(data))  # True

data = 'aab'
print(all_the_same(data))  # False

data = []
print(all_the_same(data))  # True

data = 'a'
print(all_the_same(data))  # True



print('------')

# Challenge 25  --  Extra


def read_backwards(s):
    return ' '.join(s.split(' ')[::-1])


txt = 'the love is real'
print(read_backwards(txt))  # 'real is love the'



'''
Challenge #25:

Day 25: All the Same

Create a function called all_the_same that takes one argument, a string, a list, 
or a tuple and checks if all the elements are the same. If the elements are the 
same, the function should return True. If not, it should return False. 
For example, [‘Mary’, ‘Mary’, ‘Mary’] should return True.

Extra Challenge: Reverse a String

str1 = "the love is real"

Write a function called read_backwards that takes a string as an argument and 
reverses it. For example, the string above should return: "real is love the"
'''

