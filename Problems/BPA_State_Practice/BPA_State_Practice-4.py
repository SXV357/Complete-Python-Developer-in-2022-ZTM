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
    elif len(digits) > 1 and len(digits) == 2:
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
    elif len(digits) > 2:
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
    return -1

print(letterCombinations("234"))