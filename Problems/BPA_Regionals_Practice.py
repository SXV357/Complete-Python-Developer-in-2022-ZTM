# 1
def count_occurrences(array):
    count_nineteen = 0
    count_five = 0
    for i in range(len(array)):
        if array[i] == 19:
            count_nineteen = count_nineteen + 1
        elif (array[i] == 5):
            count_five = count_five + 1
    if (count_nineteen == 2 and count_five >= 3):
        return True
    return False

# 2


def length_and_occurrences(arr):
    first_five = arr[:5]
    fifth_elem = first_five[-1]
    count_fifth = 0
    for item in range(len(arr)):
        if arr[item] == fifth_elem:
            count_fifth = count_fifth + 1
    if len(arr) == 8 and count_fifth == 3:
        return True
    return False

# 3


def calculate_piles(n):
    arr = []
    end = (n-1) * 2
    for i in range(n, end + n + 2, 2):
        arr.append(i)
    return arr


# 4
def differs_by_ten(array):
    for i in range(len(array) - 1):
        if array[i + 1] - array[i] == 10:
            return True
    return False

# 5


def sum(array):
    sum = 0
    for i in range(len(array)):
        sum += array[i]
    if sum == len(array):
        return True
    return False

# 6


def split(string):
    entire_list = []
    separator_list = []
    for i in range(len(string)):
        if string[i] == '' or string[i] == ', ':
            separator_list.append(i)
    entire_list.append(string.split())
    entire_list.append(separator_list)
    return entire_list

# 7


def distinct(array):
    count_one = array.count(1)
    count_two = array.count(2)
    count_three = array.count(3)
    count_four = array.count(4)
    for i in range(len(array) - 1):
        if count_one != 0 and count_two != 0 and count_three != 0 and count_four != 0 and array[i] != array[i + 1]:
            return True
    return False

# 8


def threshold(li, thresh):
    indices = []
    for index, value in enumerate(li):
        if value < thresh:
            indices.append([index, value])
    return indices.sort()

# 9


def is_palindrome(li):
    res = []
    for i in range(len(li)):
        if li[i] == li[i][::-1]:
            res.append(True)
        else:
            res.append(False)
    return res

# 10

# input --> [  (   prefix, (value1, value2, value3)    )   ]


def prefix(arr):
    accessor = arr[0][1]
    try:
        output_arr = []
        for i in range(len(accessor)):
            if accessor[i][:2] == arr[0][0]:
                output_arr.append(accessor[i])
        return output_arr
    except TypeError as err:
        print('Type mismatch exception')
        raise err


print(prefix([('ca', ('cat', 'car', 'fear', 'center'))]))
print(prefix([('do', ('cat', 'dog', 'shatter', 'donut', 'at', 'todo'))]
             ))
