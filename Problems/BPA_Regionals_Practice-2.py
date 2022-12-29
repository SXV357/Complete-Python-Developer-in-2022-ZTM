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
    sorted_dict = dict(sorted(dictionary.items(), key = lambda item: item[1]))
    for key in sorted_dict.keys():
        res.append(key)
    return res
