#1
def sort_singles(arr):
    singles = []
    dictionary = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
    for i in range(len(arr)):
        val = str(arr[i])
        if len(val) == 1:
            singles.append(int(val))
        elif len(val) > 1:
            ones = int(val) % 10
            singles.append(ones)
    singles.sort()
    singles.reverse()
    res = []
    for j in range(len(singles)):
        res.append(dictionary[singles[j]])
    return res

#2
def strange_list(arr):
    res = []
    arr.sort()
    res.append(min(arr))
    remaining = arr[arr.index(min(arr)) + 1: len(arr)]
    for i in range(len(remaining)):
        maxOrMin = True
        if maxOrMin:
            res.append(max(remaining))
            maxOrMin = False
        if not maxOrMin:
            res.append(min(remaining))
        remaining = [item for item in remaining if item not in res]
        if i > len(remaining):
            break
    return res

#3
def parentheses_depth(string):
    parentheses = string.split(" ")
    res = []
    for i in range(len(parentheses)):
        num_open = 0
        num_close = 0
        for j, char in enumerate(parentheses[i]):
            if char == "(":
                num_open += 1
            elif char == ")":
                num_close += 1
        if ")()(" not in parentheses[i]:
            res.append(num_open)
        else:
            res.append(int((len(parentheses[i]) - len(")()(")) / 2))
    return res