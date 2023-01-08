#1
def matching_parentheses(string):
    res = [-1] * len(string)
    for i, char in enumerate(string):
        if char == '(':
            count = 0
            for j in range(i + 1, len(string)): # starting at next char and going till end
                if string[j] == '(': # encountering another opening parentheses
                    count += 1
                elif string[j] == ')':
                    if count == 0: # if count was > 0 then we have opening parentheses
                        res[i] = j
                        res[j] = i
                        break
                    else:
                        count -= 1
    return res

#2
def find_vowels(arr):
    vowels = ['a', 'e', 'i', 'o', 'u']
    res = []
    for i in range(len(arr)):
        string = arr[i]
        vowel_string = ""
        for j in range(len(string)):
            if string[j] in vowels:
                vowel_string += string[j]
            elif string[j] == 'y' and 'y' == string[-1]:
                vowel_string += string[-1]
        res.append(vowel_string)
    return res

#3
def matching_brackets(i, j, string):
    for idx, char in enumerate(string):
        if char == "[":
            count = 0
            for k in range(idx + 1, len(string)):
                if string[k] == "[":
                    count += 1
                elif string[k] == "]":
                    if count == 0:
                        if i == idx and j == k:
                            return True
                    else:
                        count -= 1
    return False

def is_valid_substring(string):
    open_brackets = []
    close_brackets = []
    # appending the indices of all the opening and closing brackets in string
    for i in range(len(string)):
        if string[i] == "[":
            open_brackets.append(i)
        elif string[i] == "]":
            close_brackets.append(i)
    # sorting them
    open_brackets.sort()
    close_brackets.sort()
    res = []

    # Pseudocode:

    # for each item in open_brackets:
        # for each item in close_brackets:
            # compare item in close bracket to open bracket and check if those 2 indices are a matching pair
                # if True, slice the string from the index in open_bracket to index in close_bracket + 1
                # check if there's at least one opening bracket in the sliced_string
                    # if True, append that sliced string and return
    
    # checking if k > j because close comes after open(For ex: [] --> Close @ 1 and open @ 0)
    
    for j in range(len(open_brackets)):
        for k in range(len(close_brackets)):
            # Technically comparing only last three elements with values in open_brackets
            # Open = [2,4,5] Closed = [0,1,3,6,7,8]
            # 6 is compared with 2,4,5 and so on with 7 and 8
            if close_brackets[k] > open_brackets[j] and matching_brackets(j, k, string):
                 substring = string[j:k+1]
                 # to check if any open bracket hasn't been matched with a closing bracket(Lone open brackets)
                 if any(char == "[" for char in substring):
                    res.append(substring)
    return res