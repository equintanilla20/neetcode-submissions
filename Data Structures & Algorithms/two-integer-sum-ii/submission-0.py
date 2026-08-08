class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        complements = {}
        for i in range(len(numbers)):
            num = numbers[i]
            complement = target - num
            if complement in complements:
                first_index = complements[complement]
                second_index = i + 1
                return [first_index, second_index]
            complements[num] = i + 1
        return []