class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen_numbers = defaultdict(int)
        result = []
        for num in nums:
            seen_numbers[num] += 1
        while k > 0:
            max_num = 0
            max_count = -999
            for key in seen_numbers.keys():
                if seen_numbers[key] > max_count:
                    max_count = seen_numbers[key]
                    max_num = key
            del seen_numbers[max_num]
            result.append(max_num)
            k -= 1
        return result