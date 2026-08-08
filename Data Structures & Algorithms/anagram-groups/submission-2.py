class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)  # Default Dictionary value is list
        for s in strs:
            # For every string in strs
            count = [0] * 26  # list with 26 entries for every letter
            for c in s:
                # For every character in the string
                count[ord(c) - ord('a')] += 1  # Count instances of the character
            result[tuple(count)].append(s)  # Turn list into immutable tuple and append string
        return list(result.values())