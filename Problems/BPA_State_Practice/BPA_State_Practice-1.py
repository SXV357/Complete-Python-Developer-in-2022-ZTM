import random

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

print(merge_the_tools("AAABCADDE", 3))

