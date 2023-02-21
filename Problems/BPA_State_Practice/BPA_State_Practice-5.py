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

# Notes
    # --> If there's a strictly decreasing sequence after a given number, it means that all the permutations at that given state given the previous number have been exhausted
    # --> If the three potential numbers are 1/9/0 and we need to find the one after [1,9,0]
    # --> After 1, there's a strictly decreasing sequence and the next possible starting value is 9 
    # --> So, swap 1 and 9 to get 910 and since the remaining values are only 1 and 0, they need to be swapped as well since order takes precedence before forming the next possible permutation

class NextPermutation:
    # Original partially-working approach
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
    
    # Modified approach to check for strictly decreasing sequence
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
                pass
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
    
    #Approach using pointers(Most efficient time and space complexity)
    def permutationPointer(nums):
        # Case 1: If no elements present, length == 1 or length == 2
        if not nums or len(nums) == 1 or len(nums) == 2:
            nums[:] = nums.reverse()
        # We want to compare the current element with next from back to front
        pointer = len(nums) - 2
        while pointer >= 0 and nums[pointer] >= nums[pointer + 1]:
            pointer -= 1
        # If pointer is negative, it means entire array in strictly decreasing sequence
        if pointer == -1:
           return nums.reverse()
        # Swapping the number before which the decreasing sequence begins with the number at the end of the array that's supposedly +1 beyond the smaller element
        for i in range(len(nums) - 1, pointer, -1):
            if nums[pointer] < nums[i]:
                nums[pointer], nums[i] = nums[i], nums[pointer]
                break
        # Reverse the elements after the swapped element before the previously decreasing sequence
        nums[pointer + 1:] = reversed(nums[pointer + 1:])
        return nums

print(NextPermutation.permutationPointer([3,2,1]))

