# Challenge 08

def odd_even(data):
    big = max(x for x in data if not x & 1)
    small = min(x for x in data if x & 1)
    return big - small


data = [1, 2, 4, 6]
print(odd_even(data))  # 5



print('------')

# Challenge 08  --  Extra

def prime_numbers():
    limit = int(input('Enter prime number range limit: '))
    if limit < 2:
        return []
    primes = [2]
    for candidate in range(3, limit + 1, 2):
        for divisor in primes:
            flag = True
            if divisor ** 2 > candidate:
                break
            if not candidate % divisor:
                flag = False
                break
        if flag:
            primes.append(candidate)
    return primes


print(prime_numbers())  # Example 10 --> [2, 3, 5, 7]



'''
Challenge #8:

Day 8: Odd and Even

Write a function called odd_even that has one parameter and takes a list 
of numbers as an argument. The function returns the difference between the 
largest even number in the list and the smallest odd number in the list. 
For example, if you pass [1,2,4,6] as an argument the function should 
return 6 -1= 5.

Extra Challenge: List of Prime Numbers

Write a function called prime_numbers. This function asks a user to enter 
a number (integer) as an argument and returns a list of all the prime 
numbers within its range. For example, if user enters 10, your code should 
return [2, 3, 5, 7] as prime numbers.
'''

