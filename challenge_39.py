# Challenge 38


from string import printable, whitespace
from random import choices


def generate_password():
	sizes = {'W': 5, 'S': 8, 'V': 12}
	
	while 1:
		strength = input('Enter password strength (Weak, Strong or Very Strong): ')
		strength = strength.strip()[0].upper()
		if strength in sizes:
			break
	size = sizes[strength]
	
	trans = str.maketrans('', '', whitespace)
	useable = printable.translate(trans)
	pwd = choices(useable, k=size)
	return ''.join(pwd)


print(generate_password())



'''
Challenge #39:

Day 39: Password Generator

Create a function called generate_password that generates any length of 
password for the user. The password should have a random mix of upper 
letters, lower letters, numbers, and punctuation symbols. The function 
should ask the user how strong they want the password to be. The user 
should pick from - weak, strong, and very strong. If the user picks weak, 
the function should generate a 5-character long password. If the user 
picks strong, generate an 8-character password and if they pick very 
strong, generate a 12-character password.
'''

