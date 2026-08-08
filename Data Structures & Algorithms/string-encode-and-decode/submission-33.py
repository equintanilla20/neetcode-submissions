class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        elif len(strs) == 1 and strs[0] == '':
            return '\'\''
        return '|'.join(strs)

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        if s == '\'\'':
            return ['']
        return s.split('|')
