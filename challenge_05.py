# Challenge 05

def my_discount():
    price = float(input('Enter price: '))
    disc = float(input('Enter discount (%): '))
    reduced = price * (100 - disc) / 100
    return reduced


print(my_discount())
# 150 & 15 -> 127.5



print('------')

# Challenge 05  --  Extra

def gender(data):
    data = [*map(str.lower, data)]
    m = data.count('male')
    f = data.count('female')
    return [('male', m), ('female', f)]


students = ['Male', 'Female', 'female', 'male', 'male', 'male', 
            'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']

print(gender(students))
# [(‘Male’,7), (‘female’,6)]



'''
Challenge #5:

Day 5: My Discount

Create a function called my_discount. The function takes no arguments but asks 
the user to input the price and the discount (percentage) of the product. 
Once the user inputs the price and discount, it calculates the price after 
the discount. The function should return the price after the discount. 
For example, if the user enters 150 as price and 15% as the discount, 
your function should return 127.5.

Extra Challenge: Tuple of Student Sex

You work for a school and your boss wants to know how many female and male 
students are enrolled in the school. The school has saved the students in a 
list. Your task is to write a code that will count how many males and 
females are in the list. Here is a list below:

students = ['Male', 'Female', 'female', 'male', 'male', 'male',
'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']

Your code should return a list of tuples. The list above should return:
[(‘Male’,7), (‘female’,6)]
'''

