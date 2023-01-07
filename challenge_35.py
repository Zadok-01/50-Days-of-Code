# Challenge 35


from string import ascii_lowercase as small


def check_pangram(s):
    return all(letter in s.lower() for letter in small)
    # alternative
    # return not set(small) - set(s.lower())


text = 'the quick brown fox jumps over a lazy dog'
print(check_pangram(text))  # True



print('------')

# Challenge 35  --  Extra


def find_index(seq, target):
    return [ix for ix, el in enumerate(seq) if el == target] or [target] * len(seq)


seq = [1, 2, 4, 6, 7, 7]
target = 7
print(find_index(seq, target))  # [4, 5]

target = 8
print(find_index(seq, target))  # [8, 8, 8, 8, 8, 8]



'''
Challenge #35:

Day 35: Pangram

Write a function called check_pangram that takes a string and checks if it 
is a pangram. A pangram is a sentence that contains all the letters of the 
alphabet. If it is a pangram, the function should return True, otherwise, 
return False. The following sentence is a pangram so it should return True:

'the quick brown fox jumps over a lazy dog'

Extra Challenge: Find my Position

Write a function called find_index that takes two arguments; a list of 
integers, and an integer. The function should return the indexes of the 
integer in the list. If the integer is not in the list, the function should 
convert all the numbers in the list into the given integer.

For example, if the list is: [1, 2, 4, 6, 7, 7] and the integer is 7, your 
code should return [4, 5] as the indexes of 7 in the list. If the list is 
[1, 2, 4, 6, 7, 7] and the integer is 8, your code should return 
[8, 8, 8, 8, 8, 8] because 8 is not in the list.
'''

