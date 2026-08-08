class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliments = {}
        first_result = 0
        second_result = 0

        for index, num in enumerate(nums):
            compliment = target - num
            if (num + compliment) == target:
                if num not in compliments:
                    compliments[compliment] = index
                else:
                    second_result = index
                    return [compliments[num], index]
        