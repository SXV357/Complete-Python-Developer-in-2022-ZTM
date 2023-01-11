#1
def scores_increasing(arr):
    counter = 0
    for i in range(len(arr) - 1):
        if arr[i + 1] >= arr[i]:
            counter += 1
    if counter == len(arr) - 1:
        return True
    return False
#2
def scores_average(arr):
    first_half = arr[0:len(arr) // 2]
    second_half = arr[len(arr) // 2: len(arr)]
    avg_first = sum(first_half) // len(first_half)
    avg_second = sum(second_half) // len(second_half)
    return max(avg_first, avg_second)

#3
def words_without_list(arr, length):
    return [item for item in arr if len(item) != length]

#4
def has_one(num):
    string_version = str(num)
    for i in range(len(string_version)):
        if string_version[i] == "1":
            return True
    return False

#5
def divides_self(num):
    res = False
    if "0" in str(num):
        return False
    else:
        digits = list(str(num))
        for i in range(len(digits)):
            if num % int(digits[i]) == 0:
                res = True
    return res

#6
def copy_evens(arr, count):
    res = []
    evens = [i for i in arr if i % 2 == 0]
    for j in range(count):
        res.append(evens[j])
    return res

#7
def copy_endy(arr, n):
    res = []
    range_1 = [i for i in range(11)]
    range_2 = [j for j in range(90, 101)]
    endies = [val for val in arr if val in range_1 or val in range_2]
    for k in range(n):
        res.append(endies[k])
    return res

#8
def matchUp(arr1, arr2):
    counter = 0
    for i in range(len(arr1)):
        if arr1[i] != "" and arr2[i] != "":
            if arr1[i][0] == arr2[i][0]:
                counter += 1
    return counter

#9
def score_up(key, answers):
    score = 0
    for i in range(len(key)):
        if key[i] == answers[i]:
            score += 4
        elif key[i] != answers[i]:
            score -= 1
        elif key[i] and answers[i] == "?":
            score += 0
    return score

#10
def words_without(arr, target):
    return [item for item in arr if item != target]

#11
def scores_special(a1, a2):
    special_1 = [i for i in a1 if i % 10 == 0]
    special_2 = [j for j in a2 if j % 10 == 0]
    return max(special_1) + max(special_2)

#12
def sum_heights(arr, start, end):
    modified = arr[start: end + 1]
    sum = 0
    for i in range(len(modified) - 1):
        sum += abs(modified[i + 1] - modified[i])
    return sum

#13
def sum_heights2(arr, start, end):
    modified_2 = arr[start: end + 1]
    sum = 0
    for j in range(len(modified_2) - 1):
        if modified_2[j + 1] > modified_2[j]:
            sum += abs(2 * (modified_2[j + 1] - modified_2[j]))
        else:
            sum += abs(modified_2[j + 1] - modified_2[j])
    return sum

#14
def big_heights(arr, start, end):
    counter = 0
    sliced = arr[start: end + 1]
    for i in range(len(sliced) - 1):
        if not sliced[i- 1]:
            if abs(sliced[i + 1] - sliced[i]) == 5:
                counter += 1
        else:
            if abs(sliced[i] - sliced[i - 1]) == 5 or abs(sliced[i + 1] - sliced[i]) == 5:
                counter += 1
    return counter

#15
def user_compare(data):
    res = 0
    chars = [(2 * chr(i)) for i in range(97, 123) if i != 97]
    converted = list(data)
    user1 = converted[0: len(converted) // 2]
    user2 = converted[len(converted) // 2: len(converted)]
    for i in range(len(user1)):
        if (user1[i] == "aa" and user2[i] == "bb") or (user1[i] == "bb" and user2[i] in chars):
            res = -1
        elif user1[i] == "bb" and user2[i] == "aa":
            res =  1
        elif user1[i] == user2[i]:
            res = 0
    return res