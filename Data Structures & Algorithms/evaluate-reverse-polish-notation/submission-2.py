class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        st = []

        for tkn in tokens:
            if tkn not in operators:
                st.append(int(tkn))
            else:
                val1 = st.pop()
                val2 = st.pop()
                val3 = 0
                if tkn == '+':
                    val3 = val2 + val1
                if tkn == '-':
                    val3 = val2 - val1
                if tkn == '*':
                    val3 = val2 * val1
                if tkn == '/':
                    val3 = val2 / val1
                st.append(int(val3))
        return st[0]
