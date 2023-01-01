# Challenge 29


def middle_figure(a, b):
    s = ''.join((a + b).split())
    if len(s) & 1:
        return s[len(s) // 2]
    else:
        return 'no middle figure'


a = 'make love'
b = 'not wars'
print(middle_figure(a, b))  # 'e'

a, b = ' abc ', ' d '
print(middle_figure(a, b))  # 'no middle figure'

a, b = ' ab ', ' c '
print(middle_figure(a, b))  # 'b'

a, b = ' a ', ' b '
print(middle_figure(a, b))  # 'no middle figure'

a, b = ' a ', '  '
print(middle_figure(a, b))  # 'a'

a, b = '  ', '  '
print(middle_figure(a, b))  # 'no middle figure'



'''
Challenge #29:

Day 29: Middle Figure

Write a function called middle_figure that takes two parameters a, and b. 
The two parameters are strings. The function joins the two strings and 
finds the middle element. If the combined string has a middle element, 
the function should return the element, otherwise, return ‘no middle 
figure’. Use ‘make love’ as an argument for a and ‘not wars’ as an argument 
for b. Your function should return ‘e’ as the middle element. Whitespaces 
should be removed.
'''

