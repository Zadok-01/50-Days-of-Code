# Challenge 30


def repeated_name(names):
    return max(names, key=names.count)


names = ['John', 'Peter', 'John', 'Peter', 'Jones', 'Peter']
print(repeated_name(names))  # 'Peter'



print('------')

# Challenge 30  --  Extra


def sorted_names(names):
    out = []
    for name in names:
        n1, n2 = name.split()
        out.append(' '.join((n2, n1)))
    return sorted(out)


names = ['Beyonce Knowles', 'Alicia Keys', 'Katie Perry', 'Chris Brown', 'Tom Cruise']
print(sorted_names(names))
# ['Brown Chris', 'Cruise Tom', 'Keys Alicia', 'Perry Katie', 'Knowles Beyonce']



'''
Challenge #30:

Day 30: Most Repeated Name

Write a function called repeated_name that finds the most repeated name in 
the following list.

name = ["John", "Peter", "John", "Peter", "Jones", "Peter"]

Extra Challenge: Sort by Last Name

You work for a local school in your area. The school has a list of names of 
students saved in a list. The school has asked you to write a program that 
takes a list of names and sorts them alphabetically. The names should be 
sorted by last names. Here is a list of names: 

[‘Beyonce Knowles, ‘Alicia Keys’, ‘Katie Perry’, ‘Chris Brown’,’ Tom Cruise’] 

Your code should not just sort them alphabetically, but it should also 
switch the names (the last name must be the first). Here is how your code 
output should look:

['Brown Chris', 'Cruise Tom', 'Keys Alicia', 'Perry Katie', 'Knowles Beyonce']

Write a function called sorted_names.

AMENDMENT

Result should be:

['Brown Chris', 'Cruise Tom', 'Keys Alicia', 'Knowles Beyonce', 'Perry Katie']
'''

