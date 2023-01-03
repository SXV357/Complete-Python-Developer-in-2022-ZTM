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