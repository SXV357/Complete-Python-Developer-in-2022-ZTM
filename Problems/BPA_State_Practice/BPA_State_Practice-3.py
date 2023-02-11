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

if __name__ == "__main__":
    numCards = int(input())
    cards = []
    for i in range(numCards):
        card = str(input())
        cards.append(card)
    for val in cards:
        print(credit_card_validation(val))