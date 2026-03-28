class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        pairs = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        for ch in s:
            if ch in pairs.values():
                st.append(ch)
            elif ch in pairs:
                if not st or st[-1] != pairs[ch]:
                    return False
                st.pop()
        return not st
            

        