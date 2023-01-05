#1
def integer_fives(n):
    res = []
    for i in range(n):
        if "5" in str(i) and i % 9 == 0 or i % 15 == 0:
            if i % 10 == 5:
                res.append([i, 1])
            elif i % 10 != 5 and "5" in str(i):
                res.append([i, 0])
    return res

#2
def rearrange_chars(string):
    ascii_vals = []
    words = string.split(" ")
    res = []
    for i in range(len(words)):
            ascii_vals.append([ord(char) for char in words[i]])
    sorted_vals = [sorted(sub) for sub in ascii_vals]
    res.append([str(chr(sorted_vals[x][y])) for x in range(len(sorted_vals)) for y in range(len(sorted_vals[x]))])
    return ''.join(res[0])

#3
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

#4
def inject(arr, sep):
    res = []
    for i in range(0, len(arr)):
        res.append(arr[i])
        res.append(sep)
    return res[:-1]

#5
def three_sum_zero(arr):
    res = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            for k in range(i + 2, len(arr)):
                if arr[i] + arr[j] + arr[k] == 0:
                    res.append([i, j, k])
    return res
