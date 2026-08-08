class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        sequence_length = 0
        max_sequence_length = 0

        for num in nums:
            if (num - 1) not in num_set:
                sequence_length = 0
                while num + sequence_length in num_set:
                    sequence_length += 1
                max_sequence_length = max(sequence_length, max_sequence_length)
        
        return max_sequence_length
            
