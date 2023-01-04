# Challenge 32


def password_validator():
    while True:
        pwd = input('Enter passwrord \n(at least one uppercase letter, \nat least one lowercase letter \nand minimum 8 characters): ')
        
        if len(pwd) < 8:
            print(f'\n{pwd} is too short.\n')
            continue
        
        if not any(ch.isupper() for ch in pwd):
            print(f'\n{pwd} does not contain any uppercase letters.\n')
            continue
        
        if not any(ch.islower() for ch in pwd):
            print(f'\n{pwd} does not contain any lowercase letters.\n')
            continue
        
        print()
        break
    
    return pwd


print(password_validator())



print('------')

# Challenge 32  --  Extra


def email_validator(emails):
    valid = []
    
    for email in emails:
        if type(email) != str:
            continue
        
        parts = email.split('@')
        if len(parts) != 2:
            continue
        
        prefix, suffix = parts
        if not all((prefix, suffix)):
            continue
        
        if not suffix.endswith('.com'):
            continue
        
        valid.append(email)
    
    return valid if valid else 'all emails are invalid'


emails = ['ben@mail.com', 'john@mail.cm', 'kenny@gmail.com', '@list.com']
print(email_validator(emails))
# ['ben@mail.com', 'kenny@gmail.com']



'''
Challenge #32:

Day 32: Password Validator

Write a function called password_validator. The function asks the user to 
enter a password with at least one upper letter, one lower letter, 
minimum 8 characters long. If the password is valid, the function should 
return the valid password. If the password is not valid, the function 
should tell the users the errors in the password and prompt the user to 
enter another password. The code should only stop once the user enters a 
valid password.

Extra Challenge: Valid Email

emails = ['ben@mail.com', 'john@mail.cm', 'kenny@gmail.com', '@list.com' ]
((spelling corrected))

Write a function called email_validator that takes a list of emails and 
checks if the emails are valid. The function returns a list of only valid 
emails. A valid email address contains text, an '@' sign and ends with 
.com, in that order. For example, the list of emails above should output 
the following as valid emails:

['ben@mail.com', 'kenny@gmail.com']

If no emails in the list are valid, the function should return ‘all emails are invalid’
'''

