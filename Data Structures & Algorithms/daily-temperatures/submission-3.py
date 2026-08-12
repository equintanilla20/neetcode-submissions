class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stk = []

        for idx, temp in enumerate(temperatures):
            while stk and temperatures[stk[-1]] < temp:
                prev = stk.pop()
                result[prev] = idx - prev
            stk.append(idx)
            
        return result
