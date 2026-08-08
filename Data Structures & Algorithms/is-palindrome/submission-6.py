class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns = s.upper().replace(' ', '')
        i = 0
        j = len(ns)-1
        while i < j:
            if not ns[i].isalnum():
                i += 1
            if not ns[j].isalnum():
                j -= 1
            if i < j and ns[i] != ns[j]:
                return False
            i += 1
            j -= 1
        return True
        