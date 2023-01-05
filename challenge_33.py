# Challenge 33


def inter_section(a, b):
    # return tuple(set(a) & set(b))
    return tuple(x for x in a if x in b)


list1 = [20, 30, 60, 65, 75, 80, 85]
list2 = [42, 30, 80, 65, 68, 88, 95]
print(inter_section(list1, list2))  # (30, 65, 80)



print('------')

# Challenge 33  --  Extra


from time import perf_counter_ns


def search_list(limit, target):
    x = list(range(limit))
    start = perf_counter_ns()
    target in x
    finish = perf_counter_ns()
    return finish - start


def search_set(limit, target):
    x = set(range(limit))
    start = perf_counter_ns()
    target in x
    finish = perf_counter_ns()
    return finish - start


def search_range(limit, target):
    # extra option for comparison
    x = range(limit)
    start = perf_counter_ns()
    target in x
    finish = perf_counter_ns()
    return finish - start


limit = 10_000_000
target = 9_999_999
options = {search_list: 'list', search_set: 'set', search_range: 'range'}

results = []
for func in options:
    results.append((func(limit, target), options[func]))

print(results)

fastest = min(results)[1]
print(f'\nIn this exercise it is quicker to search in a {fastest}.')

# Note that the order of speed of the search only (fastest to slowest) is 
# set, range, list.
#
# However, if on includes the time to construct the data structure to be 
# searched then the order becomes
# range, list, set



'''
Challenge #33:

Day 33: List Intersection

Write a function called inter_section that takes two lists and finds the 
intersection (the elements that are present in both lists). The function 
should return a tuple of intersections. Use the lists below. Your function 
should return (30, 65, 80).

list1 = [20, 30, 60, 65, 75, 80, 85]
list2 = [ 42, 30, 80, 65, 68, 88, 95]

Extra Challenge: Set or list

You must write code that will search for a number in a range. You have a 
decision to make as to whether to store the number in a set or a list. 
Your decision will be based on time. You have to pick a data type that 
executes faster. See below:

a = range(10000000)
x = set(a)
y = list(a)

Let’s say you are looking for a number 9999999 in the range above. Search 
for this number in the list and the set. Your challenge is to find which 
code executes faster. You will pick the one that executes quicker, lists, 
or sets. Run the two searches and time them.
'''

