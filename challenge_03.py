'''
Challenge #3:
Day 3: Register Check
Write a function called register_check that checks how many students are in school. The function takes a dictionary as a parameter. If the student is in school, the dictionary says ‘yes’. If the student is not in school, the dictionary says ‘no’. Your function should return the number of students in school. Use the dictionary below. Your function should return 3.

register = {‘Michael’ : ‘yes’, ‘John’ : ‘no’ , ‘Peter’ : ‘Yes’, ‘Mary’: ‘Yes’}


Extra Challenge: Lowercase Names

names = ["kerry", "dickson", "John", "Mary", "carol", "Rose", "adam"]

You are given a list of names above. This list is made up of names of lowercase and uppercase letters. Your task is to write a code that will return a tuple of all the names in the list that have only lowercase letters. Your tuple should have names sorted alphabetically in descending order. Using the list above, your code should return:
('kerry', 'dickson', 'carol', 'adam')
'''

# Challenge 3
def register_check(reg):
	return sum(1 for v in reg.values() if v.lower() == 'yes')

register = {'Michael' : 'yes', 'John' : 'no' , 'Peter' : 'Yes', 'Mary': 'Yes'}
print(register_check(register))


# Challenge 3 - Extra
def all_lower(names):
	return tuple(n for n in names if n.islower())

names = ["kerry", "dickson", "John", "Mary", "carol", "Rose", "adam"]
print(all_lower(names))

