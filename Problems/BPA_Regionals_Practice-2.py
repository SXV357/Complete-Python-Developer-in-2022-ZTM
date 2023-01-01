# 1
def compute_product(n):
    product = 1
    string_version = str(n)
    for i in range(0, len(string_version)):
        if (int(string_version[i]) % 2) != 0:
            product *= int(string_version[i])
    return product

# 2
def largest_k_nums(arr, k):
    res = []
    arr.sort()
    for i in range(0, k):
        res.append(arr[-1])
        arr.pop(-1)
    return res

# 3
def largest_divisor(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return max(divisors)

# 4
def sum_digits(n):
    sum = 0
    string_version = str(n)
    for i in range(len(string_version)):
        number = string_version[i]
        sum = sum + int(number)
    return sum


def sort_on_sum(arr):
    sum_values = []
    dictionary = {}
    res = []
    for i in range(len(arr)):
        sum_item = sum_digits(arr[i])
        sum_values.append(sum_item)
        dictionary[arr[i]] = sum_values[i]
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1]))
    for key in sorted_dict.keys():
        res.append(key)
    return res

# 5
def sum_elems(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum


def triples_zero(arr):
    res = []
    for i in range(len(arr)):
        if sum_elems(arr[i]) == 0:
            res.append(True)
        else:
            res.append(False)
    return res

# 6

# rotate forward by 2 positions
# chr((ord(char) + 2 - 65) % 26 + 65) --> rotate upper by 2 positions
# chr(ord(char) + 2 - 97) % 26 + 97) --> rotate lower by 2 positions

def target_vowels(string):
    case_flipped = ""
    for i in range(len(string)):
        if string[i].islower():
            case_flipped += str(chr(ord(string[i]) - 32))
        elif string[i].isupper():
            case_flipped += str(chr(ord(string[i]) + 32))
    print(f'Flipped string: {case_flipped}')
    for j in range(len(case_flipped)):
        char_ascii = ord(case_flipped[j])
        if case_flipped[j] == "a" or case_flipped[j] == "e" or case_flipped[j] == "i" or case_flipped[j] == "o" or case_flipped[j] == "u":
            case_flipped[j] = str(chr((char_ascii + 2 - 97) % 26 + 97))
        elif case_flipped[j] == "A" or case_flipped[j] == "E" or case_flipped[j] == "I" or case_flipped[j] == "O" or case_flipped[j] == "U":
            case_flipped[j] = str(chr((char_ascii + 2 - 65) % 26 + 65))
    return case_flipped

#7
def sort_on_strings(string):
    res = {}
    sorted_strings = ""
    mappings = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10}
    split_values = string.split(" ")
    for i in range(len(split_values)):
        res[split_values[i]] = mappings[split_values[i]]
    sorted_results = dict(sorted(res.items(), key = lambda pair: pair[1]))
    for key in sorted_results.keys():
        sorted_strings += key + " "
    return sorted_strings

#8
def distinct_set(string):
    lower_case = string.lower()  
    chars = []
    for i in range(len(lower_case)):
        chars.append(lower_case[i])
    return list(set(chars))

#9

# ord(char) = ascii value
# chr(ascii) = character that corresponds to that ascii

def n_consonants(string, n):
    res = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = [chr(i) for i in range(97, 123) if chr(i) not in vowels]
    split_string = string.split(" ")
    for i in range(len(split_string)):
        consonant_counter = 0
        for j in range(len(split_string[i])):
            if split_string[i][j] in consonants:
                consonant_counter += 1
        if consonant_counter == n:
            res.append(split_string[i])
    return res

#10
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def hex_is_prime(string):
    res = []
    for i in range(len(string)):
        if string[i].isnumeric():
            if is_prime(int(string[i])):
                res.append(True)
            else:
                res.append(False)
        else:
            if is_prime(ord(string[i])):
                res.append(True)
            else:
                res.append(False)
    return res

#11
def even_palindromes(n):
    res = []
    for i in range(n):
        if str(i) == str(i)[::-1] and i % 2 == 0:
            res.append(i)
    return res

#12
def sum_negative(n):
    sum = 0
    string_version = str(n)
    concatenated = string_version[0] + string_version[1]
    sum += int(concatenated)
    for i in range(2, len(string_version)):
        sum += int(string_version[i])
    return sum

def sum_greater_than_zero(arr):
    res = []
    for i in range(len(arr)):
        if str(arr[i])[0] == "-":
            if sum_negative(str(arr[i])) > 0:
                res.append(int(str(arr[i])))
        else:
            if sum_digits(arr[i]) > 0:
                res.append(arr[i])
    return res

#13
def decreasing_indices(arr):
    res = []
    for i in range(len(arr) - 1):
        if arr[i + 1] > arr[i]:
            continue
        else:
            res.append([i, i + 1])
            break
    return res

#14

# count of item in the array should be equal to the number itself
# Ex: if 5 is in the array and is occurring 5 times, return 5 since it is +ve and satisfies the condition

def h_index(arr):
    arr.sort()
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] > 0 and arr.count(arr[i]) == arr[i]:
            return arr[i]
    return -1

#15
def even_length(arr):
    even = []
    dictionary = {}
    for i in range(len(arr)):
        if len(arr[i]) % 2 == 0:
            even.append(arr[i])
    for j in range(len(even)):
        dictionary[j] = even[j]
    return list(sorted(dictionary.values(), key = lambda item: len(item)))