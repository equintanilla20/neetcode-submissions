class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) == 0 or len(text2) == 0:
            return 0
        n = len(text1)
        m = len(text2)

        result = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    result[i][j] = 1 + result[i - 1][j - 1]
                else:
                    result[i][j] = max(result[i - 1][j], result[i][j - 1])
        return result[n][m]

