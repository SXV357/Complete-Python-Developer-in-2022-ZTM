from random import shuffle
import math

#1
def matching_parentheses(string):
    res = [-1] * len(string)
    for i, char in enumerate(string):
        if char == '(':
            count = 0
            for j in range(i + 1, len(string)): # starting at next char and going till end
                if string[j] == '(': # encountering another opening parentheses
                    count += 1
                elif string[j] == ')':
                    if count == 0: # if count was > 0 then we have opening parentheses
                        res[i] = j
                        res[j] = i
                        break
                    else:
                        count -= 1
    return res

#2
def find_vowels(arr):
    vowels = ['a', 'e', 'i', 'o', 'u']
    res = []
    for i in range(len(arr)):
        string = arr[i]
        vowel_string = ""
        for j in range(len(string)):
            if string[j] in vowels:
                vowel_string += string[j]
            elif string[j] == 'y' and 'y' == string[-1]:
                vowel_string += string[-1]
        res.append(vowel_string)
    return res

#3
def matching_brackets(i, j, string):
    for idx, char in enumerate(string):
        if char == "[":
            count = 0
            for k in range(idx + 1, len(string)):
                if string[k] == "[":
                    count += 1
                elif string[k] == "]":
                    if count == 0:
                        if i == idx and j == k:
                            return True
                    else:
                        count -= 1
    return False

def is_valid_substring(string):
    open_brackets = []
    close_brackets = []
    # appending the indices of all the opening and closing brackets in string
    for i in range(len(string)):
        if string[i] == "[":
            open_brackets.append(i)
        elif string[i] == "]":
            close_brackets.append(i)
    # sorting them
    open_brackets.sort()
    close_brackets.sort()
    res = []

    # Pseudocode:

    # for each item in open_brackets:
        # for each item in close_brackets:
            # compare item in close bracket to open bracket and check if those 2 indices are a matching pair
                # if True, slice the string from the index in open_bracket to index in close_bracket + 1
                # check if there's at least one opening bracket in the sliced_string
                    # if True, append that sliced string and return
    
    # checking if k > j because close comes after open(For ex: [] --> Close @ 1 and open @ 0)
    
    for j in range(len(open_brackets)):
        for k in range(len(close_brackets)):
            # Technically comparing only last three elements with values in open_brackets
            # Open = [2,4,5] Closed = [0,1,3,6,7,8]
            # 6 is compared with 2,4,5 and so on with 7 and 8
            if close_brackets[k] > open_brackets[j] and matching_brackets(j, k, string):
                 substring = string[j:k+1]
                 # to check if any open bracket hasn't been matched with a closing bracket(Lone open brackets)
                 if any(char == "[" for char in substring):
                    res.append(substring)
    return res

#4
def product_primes(n):
    res = []
    values = list(range(n))
    primes = [i for i in range(2, n) if all(i % j != 0 for j in range(2, i))]
    for value in values:
        for i in primes:
            for j in primes:
                for k in primes:
                    if i * j * k == value:
                        res.append([i, j, k])
    return res

#5
def total_appetite(arr):
    res = []
    for array in arr:
        sum = 0
        difference = 0
        sum += array[0] + array[1]
        difference = abs(array[-1] - sum)
        res.append([sum, difference])
    return res

#6
def n_digits(n):
    res = []
    for i in range(1000):
        string_version = str(i)
        digits = list(string_version)
        if (len(string_version) == n) and (digits[0] == "2" or digits[-1] == "2"):
            res.append(int(string_version))
    return res

#7
def manipulate_array(arr):
    res = []
    odd_indices = [arr[item] for item in range(len(arr)) if item % 2 != 0]
    updated_list = [val for val in arr if val not in odd_indices]
    updated_list.sort()
    # If odd_indices and updated_list have same length
    if len(odd_indices) == len(updated_list):
        matched_vals = list(zip(updated_list,odd_indices))
        for i in range(len(matched_vals)):
            for j in range(len(matched_vals[i])):
                res.append(matched_vals[i][j])
    else:
        # Where len(odd) > len(updated)
        if len(odd_indices) > len(updated_list):
            match1 = list(zip(updated_list, odd_indices))
            for i in range(len(match1)):
                for j in range(len(match1[i])):
                    res.append(match1[i][j])
            res.append(odd_indices[-1])
        # Where len(updated) > len(odd)
        elif len(updated_list) > len(odd_indices):
            match2 = list(zip(updated_list, odd_indices))
            for i in range(len(match2)):
                for j in range(len(match2[i])):
                    res.append(match2[i][j])
            res.append(updated_list[-1])
    return res

#8
def closest_palindrome(string):
    combinations = []
    lower = string.lower()
    res = ""
    chars = [chr(i) for i in range(97, 123)]
    for i in range(len(lower)):
        for j in range(len(chars)):
            modified_string = string.replace(lower[i], chars[j])
            combinations.append(modified_string)
    for combination in combinations:
        if combination == combination[::-1]:
            res = combination
    return res

#9
def matching_parentheses(i, j, string):
    for idx, char in enumerate(string):
        if char == "(":
            count = 0
            for k in range(idx + 1, len(string)):
                if string[k] == "(":
                    count += 1
                elif string[k] == ")":
                    if count == 0:
                        if i == idx and j == k:
                            return True
                    else:
                        count -= 1
    return False

def matched_whitespace(string):
    modified = string.replace(" ", "")
    opening = []
    closing = []
    for idx, chr in enumerate(modified):
        if chr == "(":
            opening.append(idx)
        elif chr == ")":
            closing.append(idx)
    opening.sort()
    closing.sort()
    res = []
    for i in opening:
        for j in closing:
            if j > i and matching_parentheses(i, j, modified):
                substring = modified[i:j+ 1]
                res.append(substring)
                break
    return list(set(res))

#10
def modify_palindrome(string, length):
    combinations = []
    shuffled = []
    extra = length - len(string)
    chars = list(string)
    for i in range(len(chars)):
        combinations.append(string + (extra * chars[i]))
    for combination in combinations:
        letters = list(combination)
        for k in range(math.factorial(len(letters))):
            shuffle(letters)
            shuffled.append(''.join(letters))
    res = ""
    for j in range(len(shuffled)):
        word = shuffled[j]
        if word == word[::-1]:
            res = word
            return res
    return "A palindrome cannot be constructed with given length from given string"