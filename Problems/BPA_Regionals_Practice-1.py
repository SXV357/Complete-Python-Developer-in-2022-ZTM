import random

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

#11
def find_lengths(array):
    res = []
    for i in range(len(array)):
        res.append(len(array[i]))
    return res

#12
def longest_string(array):
    longest = " "
    max_len = len(array[0])
    for j in range(len(array)):
        if len(array[j]) > max_len:
            max_len = len(array[j])
            longest = array[j]
    return longest

#13
def number_string(n):
    new_string = ""
    for i in range(0, n + 1):
        new_string += str(i) + " "
    return new_string

#14
def ragged_matrix(arr):
    res = []
    for i in range(len(arr[0])):
        for j in range(len(arr[0][i])):
            if arr[0][i][j] == arr[1]:
                res.append([i, j])
    return res

#15
def split(string):
    res = []
    if ' ' in string:
        res = string.split()
    elif ',' in string:
        res = string.split(',')
    else:
      res.append(string[1])
      res.append(string[3])
    return res 

#16
def check_monotonic(arr):
    res = ""
    for i in range(len(arr) - 1):
        if arr[i + 1] > arr[i]:
            res = "Increasing"
        elif (not arr[i + 1] > arr[i]) and (abs(arr[i + 1] - arr[i]) != 1):
            res = "Not a monotonic sequence"
        elif (not arr[i + 1] > arr[i]) and (abs(arr[i + 1] - arr[i]) == 1):
            res = "Decreasing"
    return res

#17
def separated(array):
    res = []
    for i in range(len(array)):
        split_arr = array[i].split(" ")
        if len(split_arr) > 1:
            res.append(True)
        else:
            res.append(False)
    return res

#18
def calc_ascii_sum(string):
    sum = 0
    for i in range(len(string)):
        if string[i].isupper():
            sum += ord(string[i])
    return sum

#19

def detect_drops(array):
    res = []
    for i in range(0, len(array) - 1):
        if array[i + 1] < array[i]:
            res.append(i + 1)
    return res

#20

def calculate_max(array: list) -> list:
    res = []
    res.append(array[0])
    for i in range(2, len(array)):
        elements = array[0:i]
        res.append(max(elements))
    return res

#21 --> Pending
def calc_XOR(arr):
    return "0b" + str((int(arr[0]) ^ int(arr[1])))

#21
def find_largest(array):
    maximum_number = 0.0
    for i in range(len(array)):
        split_string = array[i].split(",")
        if len(split_string) > 1:
            array[i] = str(split_string[0]) + "." + str(split_string[1])
        if float(array[i]) > maximum_number:
            maximum_number = float(array[i])
    return maximum_number

#22
def most_unique(arr):
    unique_strings = []
    for i in range(len(arr)):
        for j in range(len(arr[i]) - 1):
            if arr[i][j + 1] != arr[i][j]:
                unique_strings.append(arr[i])
    return random.choice(unique_strings)

#23
def sum_to_zero(array):
    indices = []
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if (array[i] + array[j]) == 0:
                indices.append([i,j])
    return indices[0]

#24
def fewer_total_chars(arr):
    chars_first = 0
    chars_second = 0
    for i in range(len(arr[0])):
        chars_first += len(arr[0][i])
    for j in range(len(arr[1])):
        chars_second += len(arr[1][j])
    if chars_first > chars_second:
        return arr[1]
    elif chars_second > chars_first:
        return arr[0]
    return arr    

#25
def find_upper_vowel(string):
    res = []
    for i in range(0, len(string), 2):
        if string[i] == 'A' or string[i] == 'E' or string[i] == 'I' or string[i] == 'O' or string[i] == 'U':
            res.append(i)
    return res

#26
def has_three_digs(n):
    digits = 0
    for i in range(len(n)):
        if n[i].isnumeric():
            digits = digits + 1
    return digits == 3


def find_k_sum(arr, k):
    sum = 0
    for i in range(0, k):
        if has_three_digs(str(arr[i])):
            sum += arr[i]
    return sum

