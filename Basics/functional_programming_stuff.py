from functools import reduce
# separation of data and functions(attributes and methods
# rules: same input will always result in same output, 
# no side effects produced(doesn't interact with the outside world)

#map(function, iterable)
def mul_2(li):
    empty_list = []
    for i in li:
        empty_list.append(i*2)
    return empty_list

print(mul_2([1,2,3,4,5]))

#cleaner way of getting same output

def multiply_items(li):
    return li * 2

print(list(map(multiply_items, [1,2,3,4,5])))
# map by default returns an object, but we're converting it into a list(takes function and iterable as input)
# map automatically calls the function and iterable is looped over and the action is taken on each item

def check_evens(li):
    return li % 2 == 0

print(tuple((map(check_evens, [1,2,3,4,5]))))

##########################################################################################

#filter(function, iterable)
new_list = list(range(101))

def check_multiples_of_6(li):
    return li % 6 == 0

print(new_list)
print(list(filter(check_multiples_of_6, new_list))) # only includes values that are true as returned by function
# all numbers that are not multiples of 6 are filtered out and not included in the new list

names = ['Andy', 'Alice', 'Alexandar', 'Anthony', 'Bobby', 'Cary', 'Johnny']

def check_first_letter(li):
    return li[0] == 'A'

print(list(filter(check_first_letter, names)))

def check_last_letter(li):
    return li[:2] == 'An'

print(list(filter(check_last_letter, names)))

##########################################################################################

#zip(iterable1, iterable2, ...)
li_1 = [58,134,23,5,17]
li_2 = [73,41,86,94,100]

print(list(zip(li_1, li_2))) # zips items of same index in both lists together and returns them as a tuple

print(list(zip(li_1[::-1], li_2[::-1])))
print(list(zip(sorted(li_1), sorted(li_2))))

usernames = ["jimbo", "giltson98", "derekf", "WhatSup"]
phone_numbers = ["8675309", "3141592", "6432123", "8312385"]

print(list(zip(usernames, phone_numbers)))

for index, item in enumerate(zip(usernames, phone_numbers)):
    print(index, item)

##########################################################################################

#reduce(function, iterable, initializer)

some_list = list(range(101))

def accumulator_func(accumulator, i):
    print(accumulator, i) # first iteration will return (0, 1) and since sum is 1
    return accumulator + i # accumulator becomes 1 after first iteration and then returns (1,2) resulting in 3

# print(reduce(accumulator_func, some_list, 0))

#########################################################################################

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def capitalize_items(li):
    return li.capitalize()

print(list(map(capitalize_items, my_pets)))

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

print(list(zip(my_strings, sorted(my_numbers))))

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def over_fifty(li):
    return li > 50

print(sorted(list(filter(over_fifty, scores))))

#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

def combine_numbers(ac, item):
    # print(ac, item)
    return ac + item

print(reduce(combine_numbers, sorted(my_numbers + scores))) # list keyword no longer required with reduce

#####################################################################################

# Use map to print the square of each numbers rounded
# to three decimal places
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

def square_nums(li):
    return round(li ** 2, 3)

print(sorted(list(map(square_nums, my_floats))))

# Use filter to print only the names that are less than
# or equal to seven letters
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]

def less_than_seven(li):
    return len(li) <= 7

print(list(filter(less_than_seven, my_names)))

# Use reduce to print the product of these numbers
my_numbers = [4, 6, 9, 23, 5]

new_my_nums = sorted(my_numbers)

def product_nums(accumulator, item):
    return accumulator * item

print(reduce(product_nums, new_my_nums))

palindrome_list = ['racecar', 'kayak', 'something', 'before', 'reddit', 'redivider']

def check_palindrome(li):
    return li == li[::-1]

print(list(filter(check_palindrome, palindrome_list)))

listA = [2, 3, 4]
listB = [10, 11, 12]

print(list(map(pow, listA, listB)))

listOfNumbers = [0, 1, 2, 3, 4]

def square(i):
    return i ** 2

def cube(i):
    return i ** 3

print(list(zip(map(square, listOfNumbers), map(cube, listOfNumbers))))