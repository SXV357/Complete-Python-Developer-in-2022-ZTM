#1
def nth_fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return nth_fibonacci(n - 1) + nth_fibonacci(n-2)

def first_n_fibonacci(n):
    res = []
    for i in range(1, n + 1):
        res.append(nth_fibonacci(i))
    return res

#2
def reverse_case(arr):
    for i in range(len(arr)):
        string = arr[i]
        for j in range(len(string)):
            if string[j].islower():
                string[j] = str(chr(ord(string[j]) - 32))
            elif string[j].isupper():
                string[j] = str(chr(ord(string[j]) + 32))
            elif string.isdigit():
                string = string[::-1]
    return arr

def reverse_case_alternate(arr):
    res = []
    for i in range(len(arr)):
        if arr[i].isalpha():
            res.append(arr[i].swapcase())
        elif arr[i].isdigit():
            res.append(arr[i][::-1])
    return res

#3
def units_product(arr):
    product = 1
    for i in range(len(arr)):
        product *= arr[i] % 10
    return product

#4
def remove_duplicates(arr):
    for i in range(len(arr) - 1, -1, -1):
        if arr.count(arr[i]) > 1:
            arr.pop(i)
    return arr

#5
def odd_first_and_last(arr):
    res = []
    for i in range(len(arr)):
        arr[i] = str(arr[i])
    greater_length = list(filter(lambda x: len(x) >= 2, arr))
    for j in range(len(greater_length)):
        if int(greater_length[j]) > 10:
            if int(greater_length[j][0]) and int(greater_length[j][-1]) % 2 != 0:
                res.append(int(greater_length[j]))
    return res

#6
def exponent(a, n):
    count = 0
    while int(n) >= a:
        count += 1
        n /= a
    return count

#7
def product_magnitude(arr):
    product = 1
    for i in range(len(arr)):
        product *= arr[i]
    sum = 0
    for j in range(len(arr)):
        sum += abs(arr[j])
    if len(str(product)) > 1:
        string_sum = str(sum)
        string_sum = "-" + string_sum
        sum = int(string_sum)
    return sum

#8
def biggest_even(m, n):
    evens = [i for i in range(m, n) if i % 2 == 0]
    return max(evens)

#9
def valid_filename(arr):
    accepted = ['txt', 'exe', 'jpg', 'png', 'dll']
    res = []
    for i in range(len(arr)):
        digit_count = 0
        split_file = arr[i].split(".")
        for j in range(len(split_file[0])):
            if split_file[0][j].isdigit():
                digit_count += 1
        if arr[i].count('.') == 1 and digit_count <= 3 and split_file[1] in accepted:
            res.append('Yes')
        else:
            res.append('No')
    return res

#10
def is_prime(n):
    if n == 0 or n == 1:
        return False
    else:
        for i in range(2, (int(n ** 0.5)) + 1):
            if n % i == 0:
                return False
    return True

def adjacent_prime(arr):
    res = []
    if is_prime(arr[1]):
        res.append(arr[0])
    if is_prime(arr[-2]):
        res.append(arr[-1])
    for i in range(1, len(arr) - 1):
        if is_prime(arr[i - 1]) or is_prime(arr[i + 1]):
            res.append(arr[i])
    remove_duplicates(res)
    return sorted(res)

#11
def check_total(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return 0 - sum

#12
def key_case(dictionary):
    res = ''
    res_dict = {}
    sum = 0
    for i in dictionary.keys():
        res_dict[i] = i.isupper()
    item_list = list(res_dict.items())
    for i in range(len(item_list)):
        for j in item_list[i]:
            if j == True:
                sum += 1
        if sum == 1:
            res = item_list[i][0]
        else:
            if False in item_list[i]:
                res = item_list[i][0] 
    return res 

#13
def odd_indices(arr):
    sum = 0
    for i in range(len(arr)):
        if i % 2 != 0:
            if arr[i] % 2 == 0:
                sum += arr[i]
    return sum

#14
def prime_length(string):
    res = []
    words = string.split(" ")
    for i in range(len(words)):
        if is_prime(len(words[i])):
            res.append(words[i])
    return ' '.join(res)

#15
def shift_decimal(number, shift):
    array = list(str(number))
    if shift > len(str(number)):
        return int(str(number)[::-1])
    elif shift == len(str(number)):
        return number
    else:
        while shift > 0:
            for i in range(len(array) - 1, -1, -1):
                temp = array[i]
                array[i] = array[i - 1]
                array[i - 1] = temp
    return ''.join(array)

#16

def closest_pair(arr):
    differences = []
    permutations = []
    dictionary = {}
    first = arr[0]
    last = arr[-1]
    first_forward = arr[1: len(arr)]
    last_backward = arr[0: len(arr) - 1]
    for i in range(len(first_forward)):
        permutations.append([first, first_forward[i]])
    for j in range(len(last_backward)):
        permutations.append([last, last_backward[j]])
    for k in range(1, len(arr) - 1):
        prev = arr[0: k]
        forward = arr[k + 1: len(arr)]
        for x in range(len(prev)):
            permutations.append([arr[k], prev[x]])
        for y in range(len(forward)):
            permutations.append([arr[k], forward[y]])
    differences = [abs(permutations[i][j + 1] - permutations[i][j]) for j in range(len(permutations[i]) - 1) for i in range(len(permutations))]
    for item in range(len(differences)):
        dictionary[differences[item]] = permutations[item]
    keys = list(dictionary.keys())
    min_diff = min(keys)
    res = dictionary[min_diff]
    return [arr.index(res[0]), arr.index(res[1])]