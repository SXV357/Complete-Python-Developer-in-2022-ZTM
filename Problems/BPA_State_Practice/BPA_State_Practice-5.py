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
class NextPermutation:
    def nextPermutation1(nums:list[int]):
        if len(nums) > 1:
            counter = 0
            for i in range(len(nums) - 1):
                if nums[i] == nums[i + 1]:
                    counter += 1
            # If every single element in nums is the same
            if counter == len(nums) - 1:
                nums[:] = nums
            else:
                permutations = list(itertools.permutations(nums))
                modified = sorted(list(set(permutations)))
                currentIndex = modified.index(tuple(nums))
                # If the input is present at the end of the array and there are no permutations that exist beyond it
                if currentIndex and currentIndex == len(modified) - 1:
                    nums[:] = sorted(nums)
                # If an element exists after the index of the current element
                elif modified[currentIndex + 1]:
                    nums[:] = modified[currentIndex + 1]
        # If length == 1 or no elements exist in the array
        elif len(nums) == 1 or not nums:
            nums[:] = nums
        return nums
    
    # Different approach
    def nextPermutation2(nums):
        # Case 1: Nums is already a strictly decreasing sequence
        counter = 0
        for i in range(len(nums) -1):
            if nums[i + 1] < nums[i]:
                counter += 1
        if counter == len(nums) - 1:
            nums[:] = sorted(nums, reverse = True)
        # Case 2: Length == 1/2
        if len(nums) == 1 or len(nums) == 2:
            nums[:] = sorted(nums, reverse = True)
        # Case 3
        else:
            for j in range(len(nums)):
                current = nums[j]
                remaining = nums[j+1:len(nums)]
                counter = 0
                if j == len(nums) - 1:
                    pass
                else:
                    for k in range(len(remaining) - 1):
                        if remaining[k+1] < remaining[k]:
                            counter += 1
                    if counter == len(remaining) - 1:
                        # Check if there's a number in remaining that's right after current
                        for val in remaining:
                            if val == current + 1:
                                current, val = val, current
                        first = nums[0:nums.index(current)]
                        remaining_modified = sorted(remaining, reverse = True)
                        nums = first.extend(remaining_modified)
        return nums

print(NextPermutation.nextPermutation2([0,1,2,10,9,4,3]))

