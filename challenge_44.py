# Challenge 44


def save_emails():
    with open('challenge_44.txt', 'w') as f:
        while 1:
            email = input('Enter email or Q to quit: ')
            if email == 'Q':
                break
            f.write(email + '\n')


def open_emails():
    with open('challenge_44.txt') as f:
        for email in f:
            print(email.strip())


save_emails()
print()
open_emails()



'''
Challenge #44:

Day 44: Save Emails

Create a function called save_emails. This function takes no arguments but 
asks the user to input email, and it saves the emails in a CSV file. The 
user can input as many emails as they want. Once they hit ‘done’ the 
function saves the emails and closes the file. Create another function 
called open_emails. This function opens and reads the content of the CSV 
file. Each email must be in its line. Here is an example of how the emails 
must be saved:

jj@gmail.com
kate@yahoo.com

and not like this: 

jj@gmail.comkate@yahoo.com
'''

