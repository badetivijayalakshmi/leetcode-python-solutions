class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = []
        
        for i in num:
            while st and k > 0 and st[-1] > i:
                st.pop()
                k -= 1
            st.append(i)
        
        while k > 0:
            st.pop()
            k -= 1

        result = ''.join(st).lstrip('0')

        if not result:
            return "0"
        return result 
        