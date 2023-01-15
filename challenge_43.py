# Challenge 43


def student_marks():
    scores = {}
    
    while 1:
        name = input('Student name (or DONE to quit): ')
        if name == 'DONE':
            print()
            break
        marks = int(input('Enter marks: '))
        scores[name] = marks
        print()
    
    for k, v in scores.items():
        print(f'{k} :\t{v}')


student_marks()



'''
Challenge #43:

Day 43: Student Marks

Write a function called student_marks that records marks achieved by 
students in a test. The function should ask the user to input the name of 
the student and then ask the user to input the marks achieved by the 
student. The information should be stored in a dictionary. The name is the 
key and the marks is the value. When the user enters done, the function 
should return a dictionary of names and values entered.
'''

