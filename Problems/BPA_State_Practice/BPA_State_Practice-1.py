import random
import math
import sys
from itertools import groupby

#1
# Notes:
    # --> Each person's score can be calculated using the given algorithm:
        # [len(string) - (number of permutations that be formed with a letter starting at index i)]
        # Example: if index == 1 == "A", there are 5 different permutations that can be formed:
            # "A", "AN", "ANA", "ANAN", "ANANA" (6 - 1 = 5 = total permutations possible)
            # repeat this for each letter depending on whether it's a consonant or vowel
def minion_game(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = [chr(i) for i in range(97, 123) if chr(i) not in vowels]
    word_letters = list(string.lower())
    consonant_substrings = []
    for j in range(len(word_letters)):
        if word_letters[j] in consonants:
            consonant_substrings.append(word_letters[j])
            for k in range(j + 1, len(word_letters)):
                remaining = word_letters[j + 1: k + 1]
                string_version = ''.join(remaining)
                consonant_substrings.append(word_letters[j] + string_version)
    final_consonant_substrings = sorted(list(set(consonant_substrings)))
    vowel_substrings = []
    for x in range(len(word_letters)):
        if word_letters[x] in vowels:
            vowel_substrings.append(word_letters[x])
            for y in range(x + 1, len(word_letters)):
                remaining = word_letters[x + 1: y + 1]
                string_version = ''.join(remaining)
                vowel_substrings.append(word_letters[x] + string_version)
    final_vowel_substrings = sorted(list(set(vowel_substrings)))
    stuart_score, kevin_score = 0,0
    res = ""
    fillers = []
    if len(final_vowel_substrings) == len(final_consonant_substrings) // 2:
        for i in range((len(final_consonant_substrings) // 2) + 1, len(final_consonant_substrings) + 1):
            fillers.append("_")
    final_vowel_substrings.extend(fillers)
    while len(final_consonant_substrings) > 0:
        stuart_choice = random.choice(final_consonant_substrings)
        kevin_choice = random.choice(final_vowel_substrings)
        stuart_score += string.lower().count(stuart_choice)
        kevin_score += string.lower().count(kevin_choice)
        final_consonant_substrings.remove(stuart_choice)
        final_vowel_substrings.remove(kevin_choice)
        if len(final_consonant_substrings) == 0 and stuart_score > kevin_score:
            res += "Stuart" + " " + str(stuart_score)
            break
        elif len(final_consonant_substrings) == 0 and stuart_score < kevin_score:
            res += "Kevin" + " " + str(kevin_score)
            break
    return res

#2

# Notes:
    # --> Outer loop can go until k while inner loop can go through each substring in the main string
    # --> Depending on whether each character in the substring has been added before to a result array, we can keep adding and return it at the end
def merge_the_tools(string, k):
    length = len(string)
    possible_substrings = []
    for i in range(0, length, k):
        substring = string[i:i+3]
        possible_substrings.append(substring)
    subsequences = [list(j) for j in possible_substrings]
    for x in range(len(subsequences)):
        for y in range(len(subsequences[x]) - 1):
            if subsequences[x].count(subsequences[x][y]) > 1 and subsequences[x][y + 1] == subsequences[x][y]:
                subsequences[x].remove(subsequences[x][y])
                break
            elif subsequences[x][y + 1] != subsequences[x][y] and subsequences[x][-1] == subsequences[x][y]:
                subsequences[x].pop(-1)
                break
            elif subsequences[x][y] == subsequences[x][y + 1] and subsequences[x][y] == subsequences[x][-1]:
                element = subsequences[x][0]
                subsequences[x].clear()
                subsequences[x][0] = element
                break
    res = ""
    for val in subsequences:
        res += ''.join(val) + "\n"
    return res

#3 + #4
def find_angle(AB, BC):
    s3 = math.sqrt(math.pow(AB, 2) + math.pow(BC, 2))
    opposite, hypotenuse = s3 / 2, BC
    return round(math.degrees(math.asin(opposite / hypotenuse)))

def disjoint_sets():
    total_happiness = 0
    length, numSets = sys.argv[1], sys.argv[2]
    arr, s1, s2 = str(input()), str(input()), str(input())
    for item in list(s1):
        if item in list(arr):
            total_happiness += 1
    for item in list(s2):
        if item in list(arr):
            total_happiness -= 1
    return total_happiness

#5
def distinct_words():
    num_words = int(input())
    words = []
    w1, w2, w3, w4 = str(input()), str(input()), str(input()), str(input())
    words.extend([w1,w2,w3,w4])
    non_duplicates = list(set(words))
    word_count = [str(words.count(i)) for i in non_duplicates]
    formatted_count = ' '.join(word_count)
    return str(len(non_duplicates)) + "\n" + formatted_count

#6
def string_compression():
    input_string = str(input())
    mappings = [list(g) for key, g in groupby(input_string)]
    compression = [(len(mapping), int(mapping[0])) for mapping in mappings]
    res = ""
    for value in compression:
        res += str(value) + " "
    return res

#7

# Notes:
    # --> Need to sort count in descending order but chars in alphabetical order
    # --> sorted(dictionary, key = lambda x: -x[1], x[0])
    # This will sort all pairs in ascending order with respect to chars and descending order w respect to nums

def company_logo(string: str):
    mappings = {}
    chars = list(set(list(string)))
    for char in chars:
        mappings[char] = string.count(char)
    pairs = []
    for key, value in mappings.items():
        pairs.append((key, value))
    # pairs = sorted(pairs, key = lambda x: x[1], reverse = True)
    most_frequent_1 = []
    most_frequent_2 = []
    # Case 1: Three items in pairs have idx[1] > 1
    for item in range(len(pairs)):
        if pairs[item][1] > 1:
            most_frequent_1.append(pairs[item])
    if len(most_frequent_1) == 3:
        descending = sorted(most_frequent_1, key = lambda x: x[1], reverse= True)
        for i in range(len(descending) - 1):
            if descending[i][1] == descending[i + 1][i]:
                if ord(descending[i][0]) > ord(descending[i + 1][0]):
                    descending[i], descending[i + 1] = descending[i + 1], descending[i]
        res = ""
        for pair in descending:
            res += str(pair) + "\n"
        return res
    # Case 2: Less than three items in pairs have idx[1] > 1
    for item in range(len(pairs)):
        if pairs[item][1] > 1:
            most_frequent_2.append(pairs[item])
        # Sub case 1: If there's only 2 items that have idx[1] > 1
    if len(most_frequent_2) == 2:
        remaining = [pair for pair in pairs if pair[1] == 1]
        most_frequent_2.extend([random.choice(remaining)])
        rearranged = sorted(most_frequent_2, key = lambda x: x[1], reverse= True)
        for j in range(len(rearranged) - 1):
            if rearranged[j][1] == rearranged[j + 1][1]:
                if ord(rearranged[j][0]) < ord(rearranged[j + 1][0]):
                    return rearranged
                else:
                    rearranged[j], rearranged[j + 1] = rearranged[j + 1], rearranged[j]
        res = ""
        for pair in rearranged:
            res += str(pair) + "\n"
        return res
        # Sub case 2: If there's only 1 item that has idx[1] > 1
    elif len(most_frequent_2) == 1:
        remaining = [pair for pair in pairs if pair[1] == 1]
        for k in range(2):
            most_frequent_2.extend([random.choice(remaining)])
        rearranged_modified = sorted(most_frequent_2, key = lambda x: x[1], reverse= True)
        for z in range(len(rearranged_modified) - 1):
            if rearranged_modified[z][1] == rearranged_modified[z + 1][1]:
                if ord(rearranged_modified[z][0]) < ord(rearranged_modified[z+ 1][0]):
                    return rearranged_modified
                else:
                    rearranged_modified[z], rearranged_modified[z + 1] = rearranged_modified[z+ 1], rearranged_modified[z]
        res = ""
        for pair in rearranged_modified:
            res += str(pair) + "\n"
        return res
    return -1

#8
def n_cubes(blocks):
    # Case 1: Odd length
    if (len(blocks)) % 2 != 0:
        middle = blocks[len(blocks) // 2]
        half_one = blocks[0:len(blocks) // 2]
        half_two = blocks[(len(blocks) // 2) + 1: len(blocks)]
        res = []
        for i in range(len(half_one)):
            for j in range(len(half_two) - 1, -1, -1):
                res.append(half_two[j])
                res.append(half_one[i])
                i += 1
                j -= 1
            break
        res.append(middle)
        if res[2] > res[0]:
            return "No"
        else:
            return "Yes"
    # Case 2: Even length
    else:
        mid = len(blocks) // 2
        half_one = blocks[0: mid]
        half_two = blocks[mid:len(blocks)]
        res = []
        for x in range(len(half_one)):
            for y in range(len(half_two) - 1, -1, -1):
                res.append(half_two[y])
                res.append(half_one[x])
                x += 1
                y -= 1
            break
        if res[2] > res[0]:
            return "No"
        else:
            return "Yes"
    return -1

print(n_cubes([4,3,2,1,3,4]))
