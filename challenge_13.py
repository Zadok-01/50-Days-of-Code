# Challenge 13

def is_valid_input(user_input):
    try:
        value = float(user_input)
    except ValueError:
        return False
    
    if value < 0:
        return False
    
    return True


def your_vat():
    price = input('Enter base price: ')
    while not is_valid_input(price):
        price = input('Try again.  (Must be positive float): ')
    price = float(price)
    
    rate = input('Enter VAT rate (%): ')
    while not is_valid_input(rate):
        rate = input('Try again.  (Must be positive float): ')
    rate = float(rate)
    
    return price * (1 + rate / 100)


print(f'Sale price: {your_vat():.2f}')  # 220, 15 --> 253



print('------')

# Challenge 13  --  Extra


def python_snakes(n):
    for i in range(1, n):
        print('@ ' * i)  # "@" looks a bit like a coiled snake!
        print()


n = 7
python_snakes(n)
'''
@ 

@ @ 

@ @ @ 

@ @ @ @ 

@ @ @ @ @ 

@ @ @ @ @ @ 

'''



'''
Challenge #13:

Day 13: Pay Your Tax

Write a function called your_vat. The function takes no parameter. The 
function asks the user to input the price of an item and VAT (vat should be 
a percentage). The function should return the price of the item plus VAT. 
If the price is 220 and, VAT is 15% your code should return a vat inclusive 
price of 253. Make sure that your code can handle ValueError. Ensure the 
code runs until valid numbers are entered. (hint: Your code should include 
a while loop).

Extra Challenge: Pyramid of Snakes

Write a function called Python_snakes that takes a number as an argument and 
creates the following shape, using the number’s range: (hint: Use the loops 
and emoji library. If you pass 7 as argument, your code should print the 
following:
☯

☯ ☯

☯ ☯ ☯

☯ ☯ ☯ ☯

☯ ☯ ☯ ☯ ☯

☯ ☯ ☯ ☯ ☯ ☯

AMENDMENT:

Hey those are not snakes.
Feel free to use any emoji you like.
'''

