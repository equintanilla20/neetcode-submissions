class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_list = list(s)
        t_list = list(t)
        s_list.sort()
        t_list.sort()
        for index, char in enumerate(s_list):
            if s_list[index] != t_list[index]:
                return False
        return True
        