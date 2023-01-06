import math

# 1
def integer_fives(n):
    res = []
    for i in range(n):
        if "5" in str(i) and i % 9 == 0 or i % 15 == 0:
            if i % 10 == 5:
                res.append([i, 1])
            elif i % 10 != 5 and "5" in str(i):
                res.append([i, 0])
    return res

# 2
def rearrange_chars(string):
    ascii_vals = []
    words = string.split(" ")
    res = []
    for i in range(len(words)):
        ascii_vals.append([ord(char) for char in words[i]])
    sorted_vals = [sorted(sub) for sub in ascii_vals]
    res.append([str(chr(sorted_vals[x][y])) for x in range(
        len(sorted_vals)) for y in range(len(sorted_vals[x]))])
    return ''.join(res[0])

# 3
def negative_balance(arr):
    res = []
    for i in range(len(arr)):
        sum = 0
        for j in range(len(arr[i])):
            sum += arr[i][j]
            if sum < 0:
                res.append(sum)
                break
    return res

# 4
def inject(arr, sep):
    res = []
    for i in range(0, len(arr)):
        res.append(arr[i])
        res.append(sep)
    return res[:-1]

# 5
def three_sum_zero(arr):
    res = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            for k in range(i + 2, len(arr)):
                if arr[i] + arr[j] + arr[k] == 0:
                    res.append([i, j, k])
    return res

# 6
def vowel_substring(string):
    vowels = ["a", "e", "i", "o", "u"]
    consonants = [str(chr(i))
                  for i in range(97, 123) if str(chr(i)) not in vowels]
    substrings = []
    res = ""
    for i in range(len(string) - 2):
        char = string[i]
        remaining = string[i + 1] + string[i + 2]
        substrings.append(char + remaining)
    for value in substrings:
        if value[0].lower() and value[-1].lower() in consonants and value[1].lower() in vowels:
            res = value
    return res

# 7
def space_counts(dictionary):
    res = ""
    items = list(dictionary.items())
    for i in range(len(items)):
        res += str((items[i][1] * items[i][0]) + " ")
    return res

# 8
def reorder_array(arr):
    sum_status = ((arr[0] + arr[-1]) % 2 == 0)
    # if sum is odd
    if not sum_status:
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
    # if sum is even
    else:
        for j in range(len(arr) - 1):
            if arr[j + 1] > arr[j]:
                temp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = temp
    return arr

# 9
def is_prime(n):
    if n == 0 or n == 1:
        return False
    else:
        for i in range(2, (int(n ** 0.5)) + 1):
            if n % i == 0:
                return False
    return True


def sum_digs_prime(arr):
    primes = []
    for i in range(len(arr)):
        if is_prime(arr[i]):
            primes.append(arr[i])
    greatest_prime = max(primes)
    string_version = str(greatest_prime)
    sum_digs = 0
    for j in range(len(string_version)):
        sum_digs = sum_digs + int(string_version[j])
    return [arr.index(greatest_prime), sum_digs]

# 10
def gpa_to_letter_grades(arr):
    conversions = {4.0: "A+", 3.7: "A", 3.4: "A-", 3.0: "B+",
                   2.7: "B", 2.4: "B-", 2.0: "C+", 1.7: "C", 1.4: "C-"}
    res = []
    for i in range(len(arr)):
        if arr[i] in conversions.keys():
            res.append(conversions[arr[i]])
        elif arr[i] > 4.0:
            res.append(conversions[4.0])
        elif arr[i] < 1.4:
            res.append("F")
        elif 3.7 < arr[i] < 4.0:
            res.append(conversions[3.7])
        elif 3.4 < arr[i] < 3.7:
            res.append(conversions[3.4])
        elif 3 < arr[i] < 3.4:
            res.append(conversions[3.0])
        elif 2.7 < arr[i] < 3.0:
            res.append(conversions[2.7])
        elif 2.4 < arr[i] < 2.7:
            res.append(conversions[2.4])
        elif 2.0 < arr[i] < 2.4:
            res.append(conversions[2.0])
        elif 1.7 < arr[i] < 2.0:
            res.append(conversions[1.7])
        elif 1.4 < arr[i] < 1.7:
            res.append(conversions[1.4])
    return res

#11
def largest_negative_and_smallest_positive(arr):
    negative = [item for item in arr if item < 0]
    positive = [item for item in arr if item > 0]
    if not positive:
        return [max(negative), 0]
    return [max(negative), min(positive)]

#12
def rounded_running_total(arr):
    res = []
    for i in range(len(arr)):
        arr[i] = math.ceil(arr[i])
    squares = [i ** 2 for i in arr]
    for j in range(len(squares)):
        sum = 0
        previous = squares[0:j+1]
        for k in range(len(previous)):
            sum += previous[k]
        res.append(sum)
    return res

#13
def binary_average(a, b):
    sum = 0
    for i in range(a, b):
        sum += i
    avg = round(sum / b - a)
    return bin(avg)

#14
def odd_sublist(arr):
    odd = [1,3,5,7,9]
    odd_nums = []
    for num in arr:
        for digit in str(num):
            if int(digit) in odd and num % 2 != 0:
                odd_nums.append(num)
    return sorted(list(set(odd_nums)))

#15
def is_happy_string(string):
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            return [i, i + 1]
    return None
