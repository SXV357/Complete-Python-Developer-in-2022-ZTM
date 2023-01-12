from collections import Counter

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

#16
def merge_two(arr1, arr2, n):
    elems = []
    for i in range(len(arr1)):
        elems.append(arr1[i])
        elems.append(arr2[i])
    modified = sorted(list(set(elems)))
    return modified[0:n]

#17
def common_two(arr1, arr2):
    elems = []
    for i in range(len(arr1)):
        elems.append(arr1[i])
    for j in range(len(arr2)):
        elems.append(arr2[j])
    counts = dict(Counter(elems))
    counter = 0
    for val in counts.values():
        if val > 1:
            counter += 1
    return counter

#18
def scores_100(arr):
    for i in range(len(arr) - 1):
        if arr[i + 1] == 100 and arr[i] == 100:
            return True
    return False

#19
def wordsCount(arr, l):
    filtered = list(filter(lambda x: len(x) == l, arr))
    return len(filtered)

#20
def scores_clump(arr):
    counter = 0
    sliced = arr[0:3]
    for i in range(len(sliced) - 1):
        if sliced[i] % 2 == 0:
            if sliced[i + 1] % 2 != 0:
                if sliced[i + 1] - sliced[i] <= 2:
                    counter += 1
            else:
                return False
        else:
            if sliced[i + 1] - sliced[i] <= 2:
                counter += 1
    if counter == len(sliced) - 1:
        return True
    return False

#21
def words_front(arr, n):
    return [arr[i] for i in range(n)]

#22
def count_YZ(string):
    counter = 0
    items = string.split()
    for i in range(len(items)):
        if items[i].endswith("y") or items[i].endswith("z"):
            counter += 1
    return counter

#23
def without_string(base, remove):
    res = []
    words = base.split()
    for i in range(len(words)):
        modified = words[i].replace(remove, "")
        res.append(modified)
    return ' '.join(res)

#24
def equalIsNot(string):
    is_combos = [i * "is" for i in range(10)]
    not_combos = [i * "not" for i in range(10)]
    count_is = 0
    count_not = 0
    if " " in string:
        words = string.split()
        for i in range(len(words)):
            if "is" == words[i] or ("is" in words[i] and words[i].count("i") == 1 and words[i].count("s") == 1):
                count_is += 1
            elif "not" == words[i] or ("not" in words[i] and words[i].count("n") == 1 and words[i].count("o") == 1 and words[i].count("t") == 1):
                count_not += 1
            elif words[i] in is_combos:
                counts = dict(Counter(words[i]))
                if all(val > 1 and val == val for val in counts.values()):
                    count_is += 1
            elif words[i] in not_combos:
                counts = dict(Counter(words[i]))
                if all(val > 1 and val == val for val in counts.values()):
                    count_not += 1
    else:
        for j in range(len(string) - 2):
            if string[j + 1] == "s" and string[j] == "i":
                count_is += 1
            elif string[j + 2] == "t" and string[j + 1] == "o" and string[j] == "n":
                count_not += 1
    return count_is == count_not

#25
def g_happy(string):
    res = False
    if string.count("g") == 1 and string[0] == "g":
        if string[1] == "g":
            res = True
    elif string.count("g") == 1 and string[-1] == "g":
        if string[-2] == "g":
            res = True
    elif string.count("g") == 2 and string[0] == "g" and string[-1] == "g":
        if string[1] == "g" and string[-2] == "g":
            res = True
        else:
            res = False
    elif string.count("g") > 2 and string[0] == "g" and string[-1] == "g":
        if string[1] == "g" and string[-2] == "g":
            sliced = string[2:-2]
            if sliced[0] != "g" and sliced[-1] != "g":
                for i in range(len(sliced) - 1):
                    if sliced[i] == "g":
                        if sliced[i + 1] == "g" or sliced[i - 1] == "g":
                            res = True
        else:
            res = False
    elif string.count("g") > 2 and string[0] == "g" and string[-1] != "g":
        if string[1] == "g":
            sliced = string[2:len(string)]
            if sliced[0] != "g" and sliced[-1] != "g":
                for j in range(len(sliced) - 1):
                    if sliced[j] == "g":
                        if sliced[j + 1] == "g" or sliced[j - 1] == "g":
                            res = True
        else:
            res = False
    elif string.count("g") > 2 and string[0] != "g" and string[-1] == "g":
        if string[-2] == "g":
            sliced = string[0:-2]
            if sliced[0] != "g" and sliced[-1] != "g":
                for k in range(len(sliced) - 1):
                    if sliced[k] == "g":
                        if sliced[k + 1] == "g" or sliced[k-1] == "g":
                            res = True
        else:
            res = False
    return res

#26

# [1,2,1,1,3]                   0     1     2     3     4
# Loop to go from start to end [1 --> 2 --> 1 --> 1 --> 3]

                            #  4      3     2     1     0
# Loop to go from end to start [3 --> 1 --> 1 --> 2 --> 1]

# If we encounter same value as arr[0] backwards, slice out array from 0 to that j + 1 and append its length to max
# Need to check as we approach an element, if its count > 1 and then do the check, else append 1 to res since its a single value
# After encountering same number in both loops, break to go back to the beginning and check for each element

def max_span(arr):
    res = []
    # Forward loop
    for i in range(len(arr)):
        #Backward loop
        for j in range(len(arr) - 1, -1, -1):
            if arr[i] != arr[j]:
                continue
            elif arr[i] == arr[j] and i != len(arr) // 2:
                sliced = arr[i: j + 1]
                res.append(len(sliced))
                break
            elif arr[i] == arr[j] and i == len(arr) // 2:
                sliced = arr[arr.index(arr[i]): j]
                res.append(len(sliced))
                break
    return max(res)

print(max_span([1, 2, 1, 1, 3]))
print(max_span([1, 4, 2, 1, 4, 1, 4]))
print(max_span([1, 4, 2, 1, 4, 4, 4]))