class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int):
        counter = 0
        if len(nums) == 1:
            return False
        if len(nums) == 2:
            if nums[0] == nums[1] and 1 <= k:
                return True
        elif len(nums) > 2:
            lp, rp = 0, len(nums) - 1
            while lp <= rp:
                if nums[lp] == nums[rp] and lp != rp and abs(lp - rp) <= k:
                    counter += 1
                if nums[lp] == nums[rp] or nums[lp] != nums[rp] and lp != rp and abs(lp - rp) > k:
                    rp -= 1
        return True if counter >= 1 else False

solution = Solution()
print(solution.containsNearbyDuplicate([1,2,3,1,2,3], 2))