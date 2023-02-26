from functools import reduce
from collections import Counter
#1

# Recursive backtracking problem
# Original Non-Working solution(Passes all sample test cases for the time being)

def combinationSum(candidates: list[int], target: int):
    if len(candidates) == 1:
        if candidates[0] > target:
            return []
        if candidates[0] == target:
            return [[candidates[0]]]
        if candidates[0] < target and candidates[0] != target:
            if target % candidates[0] != 0:
                return []
            else:
                combinations = []
                for _ in range(target // candidates[0]):
                    combinations.append(candidates[0])
                return [combinations]
    elif len(candidates) > 1:
        candidates[:] = sorted(candidates)
        combinations = []
        pairs =[[candidates[i], candidates[i+1]] for i in range(len(candidates) - 1)]
        if candidates[0] + candidates[-1] == target:
            combinations.append([candidates[0], candidates[-1]])
        for pair in pairs:
            for j in range(len(pair)):
                if pair[j] == target:
                    combinations.append([pair[j]])
                    break
                if sum(pair) == target:
                    combinations.append(pair)
                    break
                if target % pair[j] == 0:
                    values = [pair[j] for _ in range(target // pair[j])]
                    combinations.append(values)
                    remaining = [item for item in pair if item != values[0]]
                    multiple_pair_sum = [values[0]] + [remaining[0] for _ in range((target-values[0]) // remaining[0])]
                    if len(multiple_pair_sum) > 1:
                        combinations.append(multiple_pair_sum)
        if len(combinations) == 1:
            # Check for other possibilities here
            modified_vals = list(filter(lambda x: target % x != 0, candidates))
            for value in modified_vals:
                if (target - value) % 2 == 0:
                    if (target - value) % modified_vals[0] == 0:
                        combinations.append([modified_vals[0] for _ in range((target - value) // modified_vals[0])] + [value])
        nonDuplicates = list(set(tuple(y) for y in combinations))
        reConverted = [list(val) for val in nonDuplicates]
        counterFiltered = list(filter(lambda i: len(list(Counter(i).values())) > 1, reConverted))
        filteredFreq = list(list(Counter(x).values()) for x in counterFiltered)
        nonTarget = []
        while len(counterFiltered) > 0:
            for j in range(len(filteredFreq)):
                count = 0
                for k in range(len(filteredFreq[j]) - 1):
                    if filteredFreq[j][k] == filteredFreq[j][k+1]:
                        count += 1
                    if count == len(filteredFreq[j]) - 1:
                        nonTarget.append(counterFiltered[j])
                        filteredFreq.remove(filteredFreq[j])
                        break
        return [value for value in reConverted if value not in nonTarget]
                    
#2
def isStrictlyPalindromic(n: int):
    res = ''.join(list(bin(n))[2:])
    if not res == res[::-1]:
        return False
    else:
        pass

#3
class SubrectangleQueries():
    def __init__(self, rectangle: list[list[int]]):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int):
        for r in range(row1, row2 + 1):
            for c in range(col1, col2 + 1):
                self.rectangle[r][c] = newValue   

    def getValue(self, row: int, col: int):
        return self.rectangle[row][col]

#4
class ParkingSystem():
    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int):
        if carType == 1:
            if self.big >= 1:
                self.big -= 1
                return True
            else:
                return False
        elif carType == 2:
            if self.medium >= 1:
                self.medium -= 1
                return True
            else:
                return False
        elif carType == 3:
            if self.small >= 1:
                self.small -= 1
                return True
            else:
                return False
#5
def leftRigthDifference(nums: list[int]):
    if len(nums) == 1:
        return [0]
    else:
        l, r = [], []
        l.append(0)
        for i in range(1, len(nums)):
            l.append(sum(nums[0:i]))
            modifiedRight = nums[1:]
        for j in range(len(modifiedRight)):
            r.append(sum(modifiedRight[j:]))
        r.append(0)
    res = []
    for val in range(len(l)):
        res.append(abs(l[val] - r[val]))
    return res