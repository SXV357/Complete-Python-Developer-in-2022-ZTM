import random
#1
class ThreeSumClosest():
    # Original partially-working approach before implementing 2-pointer
    def threeSumClosest1(self, nums, target):
        combinations = []
        counter = 0
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                counter += 1
        if counter == len(nums) - 1:
            return nums[0]
        else:
            for x in range(len(nums)):
                for y in range(len(nums)):
                    for z in range(len(nums)):
                        combinations.append([nums[x], nums[y], nums[z]])
        mappings = {}
        for combination in combinations:
            mappings[sum(combination)] = abs(sum(combination) - target)
        minDifferences = []
        for k, v in mappings.items():
            if mappings[k] == min(mappings.values()):
                minDifferences.append([k,v])
        return random.choice(minDifferences)[0]

    # 2-pointer approach + implementation
    def threeSumClosest2(self, nums, target):
        # Keep track of the sum closest to target
        closest_sum = float('inf') 
        
        # To use 2-pointer, the array needs to be sorted
        modified = sorted(nums)

        # Fixed starting element for 2 iteration(idx[0] and idx[1])
        for i in range(len(modified) - 2):
            # One element to the right of current index and very last one
            lp, rp = i + 1, len(modified) - 1
            while lp < rp:
                # Current index + (idx + 1) + Last index
                sum = modified[i] + modified[lp] + modified[rp]
                # Closest sum initially is a very large number so closest_sum will now start approaching the actual value
                if abs(target - sum) < abs(target-closest_sum):
                    closest_sum = sum
                # Ideal case(The difference is 0 so just returning the sum)
                if sum == target:
                    return sum
                # Since nums is sorted, we want numbers from the left that have a higher value so we increment the left pointer
                elif sum < target:
                    lp += 1
                # If we want a sum to approach a smaller value, we have to decrement right pointer so that we're moving towards lower values
                else:
                    rp -= 1
        return closest_sum     

#2
def letterCombinations(digits: str):
    mappings = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    } 
    if digits == "":
        return []
    elif len(digits) == 1 and digits in mappings.keys():
        return list(mappings[digits])
    elif len(digits) == 2:
        vals = list(digits)
        alphas = []
        for val in vals:
            alphas.append(list(mappings[val]))
        res = []
        remaining = alphas[1:]
        start = alphas[0]
        for i in range(len(start)):
            letter = start[i]
            for j in range(len(remaining)):
                for k in range(len(remaining[j])):
                    res.append(letter + remaining[j][k])
        return res
    elif len(digits) == 3:
        vals = list(digits)
        alphas = []
        for val in vals:
            alphas.append(list(mappings[val]))
        res = []
        start, end = alphas[0], alphas[-1]
        remaining = alphas[1:-1]
        for i in range(len(start)):
            letter = start[i]
            for j in range(len(remaining)):
                for k in range(len(remaining[j])):
                    for l in range(len(end)):
                        res.append(letter + remaining[j][k] + end[l])
        return res
    elif len(digits) == 4:
        vals = list(digits)
        alphas = []
        for val in vals:
            alphas.append(list(mappings[val]))
        res = []
        if all(alphas):
            remaining = alphas[2:]
            pairs = []
            for i in range(len(remaining[0])):
                for j in range(len(remaining[1])):
                    pairs.append(remaining[0][i] + remaining[1][j])
            for x in range(len(alphas[0])):
                for y in range(len(alphas[1])):
                    for pair in pairs:
                        res.append(alphas[0][x] + alphas[1][y] + pair)
            return res
        elif len(alphas[2]) == 4:
            start, end = alphas[0], alphas[-1]
            middle = alphas[1:-1]
            middle_pairs = []
            for i in range(len(middle[0])):
                letter = middle[0][i]
                for j in range(len(middle[1])):
                    middle_pairs.append(letter + middle[1][j])
            if len(start) == len(end):
                for x in range(len(start)):
                    start_val = start[x]
                    for pair in middle_pairs:
                        for y in range(len(end)):
                            res.append(start_val + pair + end[y])
            return res
        elif len(alphas[2]) == 3 and len(alphas[3]) == 4:
            first, second = alphas[0], alphas[1]
            remaining = alphas[2:]
            remaining_pairs = []
            for i in range(len(remaining[0])):
                for j in range(len(remaining[1])):
                    remaining_pairs.append(remaining[0][i] + remaining[1][j])
            for x in range(len(first)):
                for y in range(len(second)):
                    for pair in remaining_pairs:
                        res.append(first[x] + second[y] + pair)
            return res
    return []

#3
class ValidParentheses():
    # Original Non-Working Approach
    def isValid1(s: str):
        numOpening = 0
        numClosing = 0
        for i in s:
            if i == "(" or i == "[" or i == "{":
                numOpening += 1
            else:
                numClosing += 1
        internal_count = 0
        similarity_score = 0
        for i in range(len(list(s)) - 1):
            if list(s)[i] == list(s)[i+1]:
                similarity_score += 1
        pairs = []
        if s in ["{", "[", "(", ")", "}", "]"] or similarity_score == len(list(s)) - 1:
            return False
        non_matched_count = 0
        for j, char in enumerate(s):
            if char == "(":
                counter = 0
                for k in range(j + 1, len(s)):
                    if s[k] == "(":
                        counter += 1
                    elif s[k] == ")":
                        if counter == 0:
                            internal_count += 1
                            pairs.append((s[j:k+1]))
                            break
                        else:
                            counter -= 1
                    elif k == len(s) - 1 and s[k] != ")":
                        non_matched_count += 1
            elif char == "[":
                counter = 0
                for k in range(j + 1, len(s)):
                    if s[k] == "[":
                        counter += 1
                    elif s[k] == "]":
                        if counter == 0:
                            internal_count += 1
                            pairs.append((s[j:k+1]))
                            break
                        else:
                            counter -= 1  
                    elif k == len(s) - 1 and s[k] != "]":
                        non_matched_count += 1
            elif char == "{":
                counter = 0
                for k in range(j + 1, len(s)):
                    if s[k] == "{":
                        counter += 1
                    elif s[k] == "}":
                        if counter == 0:
                            internal_count += 1
                            pairs.append((s[j:k+1]))
                            break
                        else:
                            counter -= 1
                    elif k == len(s) - 1 and s[k] != "}":
                        non_matched_count += 1
        match = True
        if len(pairs[0]) == 3:
            for x in range(len(pairs)):
                for y in range(len(pairs[x])):
                        if pairs[x][0] == "(" and pairs[x][2] == ")" and pairs[x][1] in ["{", "[", "(", ")", "}", "]"]:
                            match = False
                        elif pairs[x][0] == "[" and pairs[x][2] == "]" and pairs[x][1] in ["{", "[", "(", ")", "}", "]"]:
                            match = False
                        elif pairs[x][0] == "{" and pairs[x][2] == "}" and pairs[x][1] in ["{", "[", "(", ")", "}", "]"]:
                            match = False
        return match and internal_count == numClosing and non_matched_count == 0
    
    # Ideal solution using stacks
    def isValid2(s: str):
        stack = []
        mappings = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        if len(s) == 1:
            return False
        for char in s:
            if char in mappings.keys():
                if stack and stack[-1] == mappings[char]:
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)
        return True if len(stack) == 0 else False

