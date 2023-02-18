#1 + # 2
def removeDuplicates(nums):
    # This solution works but creates a new array in memory and doesn't modify in-place
    
    # nums = sorted(list(set(nums)))
    # return len(nums)

    # To modify in place
    nums[:] = sorted(set(nums))
    return len(nums)

def strStr(haystack: str, needle: str):
    if needle in haystack:
        return haystack.index(needle)
    return -1

#3
def nextPermutation(nums):
    permutations = []
    for i in range(len(nums)):
        current = nums[i]
        remaining = [val for val in nums]
        remaining.remove(current)
        permutations.append([current] + remaining)
        permutations.append([current] + remaining[::-1])
    modified = sorted([list(x) for x in set(tuple(element) for element in permutations)])
    currentIndex = modified.index(nums)
    if currentIndex == len(modified) - 1:
        nums[:] = sorted(nums)
    elif currentIndex != len(modified) - 1:
        nums[:] = modified[currentIndex + 1]
    return permutations

print(nextPermutation([5,4,7,5,3,2]))