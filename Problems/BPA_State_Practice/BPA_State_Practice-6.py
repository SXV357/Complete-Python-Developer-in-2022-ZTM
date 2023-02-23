from functools import reduce
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
                for i in range(target // candidates[0]):
                    combinations.append(candidates[0])
                return [combinations]
    elif len(candidates) > 1:
        candidates[:] = sorted(candidates)
        combos = []
        # Case 1: If there's any value that's equal to target
        if target in candidates:
            combos.append([target])
        else:
            # Case 2: Check if any 2 numbers add to target
            for i in range(len(candidates) - 1):
                if candidates[i] + candidates[i+1] == target:
                    combos.append([candidates[i], candidates[i+1]])
            # Case 3: If there's a num multiplied by itself n times equals target
            values = [item for item in candidates if target % item == 0]
            if len(values) == 1:
                res = [values[0] for _ in range(target // values[0])]
                combos.append(res)
                # If (n x someNumber) + someOtherNumber == target
                running_sum, remaining = 0, [num for num in candidates if num != res[0]]
                for j in range(len(remaining)):
                    start = remaining[j]
                    for k in range(len(res)):
                        running_sum += res[k]
                        if running_sum + start == target:
                            first = (running_sum // res[0]) * [res[0]]
                            combos.append(first + [start])
        return combos
                
print(combinationSum([2], 1))
