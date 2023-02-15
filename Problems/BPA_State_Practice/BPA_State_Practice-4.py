import random
#1
def threeSumClosest(nums, target):
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

print(threeSumClosest([-1,2,-1,4], 1))