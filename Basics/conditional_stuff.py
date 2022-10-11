# ternary operator
from re import S


some_num = 20
final_statement = "less than 10" if some_num < 10 else "greater than 10"
print(final_statement)

new_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dup_arr = new_arr[:]
dup_arr.append(11)
check_condition = "equal" if len(new_arr) == len(dup_arr) and new_arr[0] == dup_arr[0] else "not equal"
print(check_condition)


is_magician = False
is_expert = True

if is_magician and is_expert:
    print("You are a master magician!")
elif is_magician and not is_expert:
    print("At least you're getting there")
elif not is_magician and is_expert:
    print("You need magic powers")
else:
    print("You\'re an L")

# is keyword checks if both values stored in same location in memory
print(False is [1,2,3]) # returns false because both values stored in diff places in memory
# data structures always created in a new location
arr1 = [1, 2, 3]
arr2 = arr1[:]
arr2.append(4)
print(arr1 is arr2)

#methods to iterate over dictionaries
#1. .keys()
#2. .values()
#3. .items()
user = {
    "name": "John",
    "age": 30,
    "is_new": True
}
for k,v in user.items():
    print(k,v)
# for x in user.items():
#     print(x)

summation = 0
my_list = [1,2,3,4,5,6,7,8,9,10]
for i in my_list:
    summation += i
print(summation)



some_list = list(range(0,1001))
new_list =[]
for i in some_list:
   for j in some_list:
      if i * j == 1000:
        print(i,j)
        new_list.append(i)
        break
print(sorted(new_list))

# reverse a range loop-over

for x in list(range(1000, 0, -20)):
    print(x)

#trick to create a new array

for x in range(10):
    print(list(range(26))) # printing a list from 0-25 10 times

# if you want index counter of item looping over, use enumerate()
for i, c in enumerate("Shreyas Viswanathan"):
    print(i, c)

for i, char in enumerate(list(range(100))):
    if char == 50:
        print('The index of 50 is {}'.format(i))

new_dict = {
    "username": "ShreyasV",
    "age": 17
}
for index, key in enumerate(new_dict.items()):
    print(index, key)


#Display the image below to the right hand side where the 0 is going to be ' ', 
# and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

for r in picture:
    for i in r:
        if i == 1:
            print('*', end = '') # to avoid new space after every execution of the print statement
        else:
            print(' ', end = '')
    print('') # for new line after every row


some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicate_list = []
for item in some_list:
    if some_list.count(item) > 1:
        if item not in duplicate_list:
            duplicate_list.append(item)

print(duplicate_list)