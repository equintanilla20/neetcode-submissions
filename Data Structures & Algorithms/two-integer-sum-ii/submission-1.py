class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        complements = {}
        for i in range(len(numbers)):
            complement = target - numbers[i]
            if complement in complements:
                return [complements[complement], i + 1]
            complements[numbers[i]] = i + 1
        return []