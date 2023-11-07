# Challenge 47


from json import dump, load


def save_json(data, file):
    with open(file, 'w') as f:
        dump(data, f)


def read_json(file):
    with open(file) as f:
        return load(f)


names = {'name': 'Carol', 'sex': 'female', 'age': 55}
file = 'challenge_47_names.json'
save_json(names, file)


names = read_json(file)
print(names)



'''
Challenge #47:

Day 47: Save a JSON

Write a function called save_json. This function takes a dictionary below 
as an argument and saves it on a file in JSON format.

Write another function called read_json that opens the file that you just 
saved and reads its content.

names = {'name': 'Carol','sex': 'female','age': 55}
'''

