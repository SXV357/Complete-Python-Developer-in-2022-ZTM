from functools import reduce
from math import factorial# general format
# lambda parameter: action to be taken on parameter(expression)

new_list = [1,2,3,4,5]

print(list(map(lambda i: i * 2, new_list))) # lambda is one time anonymous function
# instead of defining a new function from scratch, lambda can be used

print(list(filter(lambda x: x % 2 != 0, new_list))) # returns 1, 3, 5
print(reduce(lambda acc, i: acc + i, new_list)) # returns 15

#square items in list
my_list = [5,4,3]
print(list(map(lambda i: i ** 2, my_list)))

#list sorting
a = [(0,2), (4,3), (9,9), (10,-1)]
print(sorted(a, key=lambda x: x[1]))
#alternate way
a.sort(key = lambda x: x[1])
print(a)

#############################################################################################

#Problems

phones = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, 
{'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
{'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

phones.sort(key = lambda i: int(i['model']))
print(phones)
###########################################
arr_1 = [1,2,3,5,7,8,9,10]
arr_2 = [1,2,4,8,9]

print(list(filter(lambda i: i in arr_1, arr_2)))
##########################################################
li_1 = [1,2,3]
li_2 = [4,5,6]

print(list(map(lambda l1, l2: l1 + l2, li_1, li_2)))
################################################
original_list = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]

print(sorted(list(filter(lambda x: x % 13 == 0 or x % 19 == 0, original_list))))
#######################################################

string_list = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']

print(list(filter(lambda x: x == x[::-1], string_list)))
#############################################################

new_string = 'sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5'
new_array = new_string.split()
numbers_arr = []
for i in new_array:
    if i.isdigit():
        numbers_arr.append(i)

integer_list = list(map(int, numbers_arr))
print(sorted(filter(lambda x: x > len(new_array), integer_list)))
#############################################################

given_list = [2, 4, 6, 9, 11]
target = 2

print(list(map(lambda i: i * target, given_list)))
#############################################################

sample_names = ['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']
for i in sample_names:
    if i[0].islower():
        sample_names.remove(i)

def sum_of_lengths_of_names(names):
    return sum(map(lambda x: len(x) , names))

print(sum_of_lengths_of_names(sample_names))


some_names = ['Sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'Keith', 'Shreyas', 'Harsh']

def rem_cert_lens(li):
    return list(filter(lambda x: len(x) > 5 and not x[0].islower() , li))

print(sorted(rem_cert_lens(some_names), key = lambda i: i[::-1]))

new_li = list(range(int(10001 / 2)))
def manipulate_list(li):
    return list(map(lambda x: factorial(x) > 100000, li))

print(manipulate_list(new_li)[::-1])