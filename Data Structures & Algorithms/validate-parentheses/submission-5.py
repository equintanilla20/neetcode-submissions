class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False
        stk = []
        for c in s:
            if (c == '['
                    or c == '('
                    or c == '{'):
                stk.append(c)
            elif c == ']' and len(stk) > 0 and stk[-1] == '[':
                stk.pop()
            elif c == ')' and len(stk) > 0 and stk[-1] == '(':
                stk.pop()
            elif c == '}' and len(stk) > 0 and stk[-1] == '{':
                stk.pop()
            else:
                return False
        if len(stk) > 0:
            return False
        return True
                