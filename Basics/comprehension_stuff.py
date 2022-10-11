
import math
# list comprehension
my_list = [num ** 2 for num in range(0, 101) if num % 2 == 0]
print(my_list)

#set and dictionary comprehension

name_list = ['Bob', 'Randy', 'Sue', 'Mary', 'Sally']
new_set = {i for i in name_list if len(i) > 4}
print(new_set)

old_dict = {
    'n1': 4,
    'n2': 5,
    'n3': 6,
    'n4': 7,
    'n5': 8,
}
new_dict = {key: round(math.cos(value), 3) for key, value in old_dict.items()}
print(new_dict)

my_dict = {i: i * 2 for i in [1,2,3]}
print(my_dict)

# ###############################################################################

# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
# duplicate_items = sorted(list({i for i in some_list if some_list.count(i) > 1}))
# print(duplicate_items)

###############################################################################

divisible_by_seven = [x for x in range(1001) if x % 7 == 0]
print(divisible_by_seven)
###############################################################################
has_three = [x for x in range(1001) if str(x).count('3') > 0]
print(has_three)
###############################################################################
some_string = 'tp Gth b1 HmU' 
count_spaces_in_string = [x for x in some_string if x == ' ']
print(len(count_spaces_in_string))
###############################################################################
vowels = ['a', 'e', 'i', 'o', 'u']
new_string = 'Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams'

all_consonants = [x for x in new_string if x not in vowels]
print(all_consonants)
###############################################################################
new_list = ['hi', 4, 8.99, 'apple', ('t', 'b', 'n')]
some_new_list = {index:value for index, value in enumerate(new_list)}
print(some_new_list)
###############################################################################
list_a = [1,2,3,4]
list_b = [2,3,4,5]

common_items = [x for x in list_a if x in list_b]
print(common_items)
###############################################################################

sentence = 'In 1984 there were 13 instances of a protest with over 1000 people attending'

only_nums = sorted([int(x) for x in sentence.split() if x.isdigit()])
print(only_nums)
###############################################################################
evens_and_odds = ['even' if x % 2 == 0 else 'odd' for x in range(1, 21)]
print(evens_and_odds)
###############################################################################
some_sentence = 'I am a sentence'
less_than_four = [x for x in some_sentence.split() if len(x) < 4]
print(less_than_four)


