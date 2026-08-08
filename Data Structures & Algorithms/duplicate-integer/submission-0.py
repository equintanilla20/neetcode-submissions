class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_nums = {}
        for num in nums:
            if num not in seen_nums.keys():
                seen_nums[num] = 1
            else:
                return True
        return False