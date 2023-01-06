# Challenge 34


def just_digits(file):
	# nasty one-liner just for fun
	return [word for word in open(file).read().split() if word.isnumeric()]


file = 'ch34_python.txt'
print(just_digits(file))  # ['1991', '2', '200', '3', '2008']



'''
Challenge #34:

Day 34: Just Digits

In this challenge, copy the text below and save it as a CSV file. Save it 
in the same folder as your Python file. Save it as python.csv.

Write a function called just_digits that reads the text from the CSV file 
and returns only digit elements from the file. Your function should return 
1991, 2, 200, 3, 2008 as a list of strings.

“Python was released in 1991 for the first time. Python 2 was released in 
2000 and introduced new features, such as list comprehensions and a 
cycle-detecting garbage collection system (in addition to reference 
counting). Python 3 was released in 2008 and was a major revision of the 
language that is not completely backward-compatible.”

Source: Wikipedia

AMENDMENT

Text file saved as "python.txt".
'''

