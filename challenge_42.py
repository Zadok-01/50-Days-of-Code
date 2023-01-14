# Challenge 42


from textblob import TextBlob


def spelling_checker():
    while 1:
        word = input('Enter a word: ').strip()
        possible = TextBlob(word).correct()
        if word == possible:
            return word
        else:
            reply = input(f'Did you mean {possible}? (Y/N): ')
            reply = reply.strip().upper()[0]
            if reply == 'Y':
                return possible
            else:
                print('Try again.')


print(spelling_checker())



print('------')

# Challenge 42  --  Extra


from datetime import datetime, date, time, timedelta
from winsound import Beep


def alarm():
    while 1:
        setting = input('Enter valid alarm time (hh:mm): ')
        if ':' not in setting:
            continue
        setting = setting.split(':')
        if len(setting) != 2:
            continue
        hrs, mins = setting
        try:
            hrs, mins = int(hrs), int(mins)
        except ValueError:
            pass
        if (0 <= hrs < 24) and (0 <= mins < 60):
            break
    
    alarm = time(hrs, mins)
    print(f'\nAlarm set for {alarm.strftime("%H:%M")}.\n')
    
    while 1:
        diff = datetime.combine(date.today(), alarm) - datetime.now()
        if diff < timedelta():
            Beep(600, 1000)
            break


alarm()



'''
Challenge #42:

Day 42: Spelling Checker

Write a function called spelling_checker. This code asks the user to input 
a word and if a user inputs a wrong spelling it should suggest the correct 
spelling by asking the user if they meant to type that word. If the user 
says no, it should ask the user to enter the word again. If the user says 
yes, it should return the correct word. If the word entered by the user is 
correctly spelled the function should return the correct word. Use the 
module textblob.

Extra Challenge: Create an Alarm Clock

Create a function called alarm that sets an alarm clock for the user. The 
function should ask the user to enter time they want the alarm to go off. 
The user should enter the hour and minute. The function should then print 
out the time when the alarm will go off. When its alarm time, the code 
should let off a sound. Use the winsound module for sound.
'''

