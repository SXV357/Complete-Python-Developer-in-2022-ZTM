import itertools
import collections

# 1 + # 2


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

# 3

# Notes
    # --> If there's a strictly decreasing sequence after a given number, it means that all the permutations at that given state given the previous number have been exhausted
    # --> If the three potential numbers are 1/9/0 and we need to find the one after [1,9,0]
    # --> After 1, there's a strictly decreasing sequence and the next possible starting value is 9
    # --> So, swap 1 and 9 to get 910 and since the remaining values are only 1 and 0, they need to be swapped as well since order takes precedence before forming the next possible permutation


class NextPermutation:
    # Original partially-working approach
    def nextPermutation1(nums: list[int]):
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
        for i in range(len(nums) - 1):
            if nums[i + 1] < nums[i]:
                counter += 1
        if counter == len(nums) - 1:
            nums[:] = sorted(nums, reverse=True)
        # Case 2: Length == 1/2
        if len(nums) == 1 or len(nums) == 2:
            nums[:] = sorted(nums, reverse=True)
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
                        remaining_modified = sorted(remaining, reverse=True)
                        nums = first.extend(remaining_modified)
        return nums

    # Approach using pointers(Most efficient time and space complexity)
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

# 4

# Notes: Use 2-pointers(One at start and one at end and search if they equal target)


def searchRange(nums, target):
    if target in nums:
        if len(nums) == 1:
            return 2 * [0]
        elif len(nums) > 1:
            p1, p2 = 0, len(nums) - 1
            while p1 <= p2:
                if nums[p1] == target and nums[p2] == target:
                    return [p1, p2]
                if nums[p1] == target and nums[p2] != target:
                    p2 -= 1
                elif nums[p1] != target and nums[p2] == target:
                    p1 += 1
                else:
                    p1 += 1
                    p2 -= 1
    return [-1, -1]

# 5

def isValid(row: list[str]):
    default_vals = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    res = []
    row = [i for i in sorted(row) if i.isdigit()]
    for value in row:
        if value not in res and int(value) in default_vals:
            res.append(value)
        elif value in res and int(value) in default_vals:
            return False
    return True

def generateSubArrays(board: list[list[str]]):
    sub1, sub2, sub3, sub4, sub5, sub6, sub7, sub8, sub9 = [], [], [], [], [], [], [], [], []
    for r in range(3):
        res = []
        for c in range(3):
            res.append(board[r][c])
            if c == 2:
                sub1.append(res)
                break
    for r in range(3):
        res = []
        for c in range(3, 6):
            res.append(board[r][c])
            if c == 5:
                sub2.append(res)
                break
    for r in range(3):
        res = []
        for c in range(6,9):
            res.append(board[r][c])
            if c == 8:
                sub3.append(res)
                break
    for r in range(3,6):
        res = []
        for c in range(3):
            res.append(board[r][c])
            if c == 2:
                sub4.append(res)
                break
    for r in range(3,6):
        res = []
        for c in range(3,6):
            res.append(board[r][c])
            if c == 5:
                sub5.append(res)
                break
    for r in range(3,6):
        res = []
        for c in range(6,9):
            res.append(board[r][c])
            if c == 8:
                sub6.append(res)
                break
    for r in range(6,9):
        res = []
        for c in range(3):
            res.append(board[r][c])
            if c == 2:
                sub7.append(res)
                break
    for r in range(6,9):
        res = []
        for c in range(3,6):
            res.append(board[r][c])
            if c == 5:
                sub8.append(res)
                break
    for r in range(6,9):
        res = []
        for c in range(6,9):
            res.append(board[r][c])
            if c == 8:
                sub9.append(res)
                break
    modified = [list(collections.Counter([i for i in sorted(sub1[0] + sub1[1] + sub1[2]) if i.isdigit()]).values()),
                list(collections.Counter([i for i in sorted(sub2[0] + sub2[1] + sub2[2]) if i.isdigit()]).values()),
                list(collections.Counter([i for i in sorted(sub3[0] + sub3[1] + sub3[2]) if i.isdigit()]).values()),
                list(collections.Counter([i for i in sorted(sub4[0] + sub4[1] + sub4[2]) if i.isdigit()]).values()),
                list(collections.Counter([i for i in sorted(sub5[0] + sub5[1] + sub5[2]) if i.isdigit()]).values()),
                list(collections.Counter([i for i in sorted(sub6[0] + sub6[1] + sub6[2]) if i.isdigit()]).values()),
                list(collections.Counter([i for i in sorted(sub7[0] + sub7[1] + sub7[2]) if i.isdigit()]).values()),
                list(collections.Counter([i for i in sorted(sub8[0] + sub8[1] + sub8[2]) if i.isdigit()]).values()),
                list(collections.Counter([i for i in sorted(sub9[0] + sub9[1] + sub9[2]) if i.isdigit()]).values())]
    noDuplicates = 0
    for x in range(len(modified)):
        for y in range(len(modified[x])):
            if modified[x][y] == 1:
                noDuplicates += 1
    total_len = sum(len(subArr) for subArr in modified)
    return noDuplicates == total_len

class Solution():
    def isValidSudoku(board: list[list[str]]):
        columns = []
        for column in range(9):
            res = []
            for row in range(9):
                res.append(board[row][column])
                if row == 8:
                    columns.append(res)
                    break
        numValidRows = 0
        numValidCols = 0
        for row in board:
            if isValid(row):
                numValidRows += 1
        for col in columns:
            if isValid(col):
                numValidCols += 1
        return generateSubArrays(board) and numValidRows == len(board) and numValidCols == len(board)