class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        li = [1] * (n)
        
        for i in range(1, n):
            for j in range(0, i):
                if nums[j] < nums[i] and li[i] < 1 + li[j]: 
                    li[i] = 1 + li[j]

        max = 0
        for i in range(1, n):
            if li[i] > li[max]:
                max = i
        
        return li[max]