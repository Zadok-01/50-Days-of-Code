# Challenge 20


# conventional solution
'''
def capitalize(s):
    return s.title()
'''

# alternative solution
capitalize = str.title


text = 'i like learning'
print(capitalize(text))  # 'I Like Learning'



print('------')

# Challenge 20  --  Extra


def reverse_uppercase(s):
    # return [wd[::-1] for wd in s.split() if any(ch.isupper() for ch in wd)]
    return [wd[::-1] for wd in s.split() if wd.islower() is False]


text = 'leArning is hard, bUt if You appLy youRself you can achieVe success'
print(reverse_uppercase(text))
# ['gninrAel', 'tUb', 'uoY', 'yLppa', 'flesRuoy', 'eVeihca']



'''
Challenge #20:

Day 20: Capitalize First Letter

Write a function called capitalize. This function takes a string as an 
argument and capitalizes the first letter of each word. For example, 
‘i like learning’ becomes ‘I Like Learning’.

Extra Challenge: Reversed List

str1 = 'leArning is hard, bUt if You appLy youRself you can achieVe success'

You are given a string of words. Some of the words in the string contain 
uppercase letters. Write a code that will return all the words that have an 
uppercase letter. Your code should return a list of the words. Each word in 
the list should be reversed. Here is how your output should look:

['gninrAel', 'tUb', 'uoY', 'yLppa', 'flesRuoy', 'eVeihca']
'''

