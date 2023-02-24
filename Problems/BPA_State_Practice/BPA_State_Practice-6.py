from functools import reduce
from collections import Counter
#1
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
        freqFiltered = list(filter(lambda vals: len(list(Counter(vals).values())) > 1,reConverted))
        return [a for a in reConverted]

print(combinationSum([2,3], 6))