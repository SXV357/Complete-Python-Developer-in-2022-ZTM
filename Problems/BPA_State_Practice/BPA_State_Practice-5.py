import itertools

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
    if len(nums) > 1:
        counter = 0
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                counter += 1
        if counter == len(nums) - 1:
            nums[:] = nums
        else:
            permutations = list(itertools.permutations(nums))
            modified = sorted(list(set(permutations)))
            currentIndex = modified.index(tuple(nums))
            if currentIndex and currentIndex == len(modified) - 1:
                nums[:] = sorted(nums)
            elif modified[currentIndex + 1]:
                nums[:] = modified[currentIndex + 1]
    else:
        nums[:] = nums
    return nums

print(nextPermutation([6,7,5,3,5,6,2,9,1,2,7,0,9]))