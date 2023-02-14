import re
from functools import reduce
#1

# Notes
    # --> (?<=)\&\&(?=) will match all occurrences of && in the string with the replacement
    # --> Searches from start to end and once it finds this pair with spaces on either side, it replaces it

def replace_strings(string):
    pattern1 = "&&"
    pattern2 = "||"
    if len(re.findall(pattern1, string)) >= 1:
        splitted = string.split("&&")
        chars = list(splitted[0])
        if re.search(r"[&&]{2}[&]", string) or chars[-1] != ' ':
            pass
        else:
            string = re.sub("[&&]{2}", "and", string)
    elif len(re.findall(pattern2, string)) >= 1:
        splitted2 = string.split("||")
        chars2 = list(splitted2[0])
        if re.search(r"[||]{2}[|]", string):
            pass
        elif not re.search(r"[||]{2}[|]", string) or chars2[-1] != ' ':
            pass
        else:
            string = re.sub("[||]{2}", "or", string)
    return string

def string_replace_tester():
    lines = int(input())
    sentences = []
    for i in range(lines):
        sentence = input()
        sentences.append(sentence)
    res = list(map(replace_strings, sentences))
    for val in res:
        print(val, end = "\n")

#2
def credit_card_validation(string):
    validNums = [str(i) for i in range(10)]
    hasStart = (string[0] == "4" or string[0] == "5" or string[0] == "6")
    hasLength = (len(string) == 16)
    hasDigits = True
    strictSpacing = (" " not in string and "_" not in string)
    isRepeating = True
    nonHyphenRepeating = True
    if "-" in string:
        digits = []
        for i in range(len(string)):
            if string[i].isdigit():
                digits.append(string[i])
        for val in digits:
            if val in validNums:
                hasDigits = True
    else:
        for val in string:
            if val in validNums:
                hasDigits = True
    if "-" in string and strictSpacing:
        modified = string.split("-")
        pairs = {}
        for i in range(len(modified)):
            count = 0
            if len(modified[i]) < 4:
                return "Invalid"
            else:
                for j in range(len(modified[i]) - 1):
                    if int(modified[i][j]) == int(modified[i][j + 1]):
                        count += 1
                pairs[modified[i]] = count
        for k, v in pairs.items():
            if v == len(k) - 1:
                isRepeating = False
    elif not "-" in string and strictSpacing:
        if hasLength:
            groups = []
            pairs2 = {}
            for i in range(0, len(string), 4):
                groups.append(string[i:i+4])
            for x in range(len(groups)):
                count = 0
                for y in range(len(groups[x]) - 1):
                    if int(groups[x][y]) == int(groups[x][y + 1]):
                        count += 1
                pairs2[groups[x]] = count
        for k, v in pairs2.items():
            if v == len(k) - 1:
                nonHyphenRepeating = False
    if hasStart and hasLength and hasDigits and strictSpacing and isRepeating and nonHyphenRepeating:
        return "Valid"
    else:
        return "Invalid"

def card_validation_tester():
    numCards = int(input())
    cards = []
    for i in range(numCards):
        card = str(input())
        cards.append(card)
    for val in cards:
        print(credit_card_validation(val))

#3
def score_words(words):
    vowels = ["a", "e", "i", "o", "u", "y"]
    total_score = 0
    for i in range(len(words)):
        vowelCount = 0
        for j in range(len(words[i])):
            if words[i][j] in vowels:
                vowelCount += 1
        if vowelCount % 2 == 0:
            total_score += 2
        else:
            total_score += 1
    return total_score

def score_words_tester():
    numWords = int(input())
    words = []
    for _ in range(numWords):
        words.append("_")
    words = list(map(str, input().split()))
    print(score_words(words))

#4
def print_from_stream(n, stream):
    odds = [val for val in range(1,11) if val % 2 != 0]
    evens = [val for val in range(11) if val % 2 == 0]
    if stream == "even":
        for i in range(n):
            print(evens[i], end = "\n")
    elif stream == "odd":
        for i in range(n):
            print(odds[i], end = "\n")

def stream_tester():
    queries = int(input())
    cases = []
    for _ in range(queries):
        pair = list(map(str, input().split()))
        cases.append(pair)
    for i in range(len(cases)):
        for j in range(len(cases[i]) - 1):
            cases[i][j], cases[i][j + 1] = cases[i][j + 1], cases[i][j]
    for x in range(len(cases)):
        for _ in range(len(cases[x])):
            print_from_stream(int(cases[x][0]), cases[x][1])
            break

#5

# strs = ["flower", "flow", "flight"]

def longestCommonPrefix(strs):
    res = []
    for i in range(len(strs)):
        res.append(list(strs[i]))
    modified = sorted(res, key = lambda x: len(x), reverse = True)[0]
    for val in range(len(res)):
        if len(res[val]) < len(modified):
            for j in range(len(res[val]) + 1, len(modified) + 1):
                res[val].append("_")
    common = []
    remaining = res[1:len(res)]
    x = 0
    z = 0
    while x < len(res[0]):
        letter = res[0][x]
        first = []
        for y in range(len(remaining)):
            while z < len(remaining[y]):
                first.append(remaining[y][z])
                break
            if len(first) == len(remaining):
                if all(first):
                    if first[0] == letter:
                        common.append(first[0])
                        x += 1
                        z += 1
                        break
                    else:
                        return ""
    prefix = ''.join(common)
    return prefix

print(longestCommonPrefix(["flower","flow","flight"]))