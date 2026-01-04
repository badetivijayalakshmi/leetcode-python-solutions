class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        u_set = set()
        l = 0
        ans = 0
        for r in range(len(s)):
            ch = s[r]
            if ch not in u_set:
                u_set.add(ch)
            else:
                while ch in u_set:
                    u_set.remove(s[l])
                    l+=1
                u_set.add(ch)

            ans = max(ans,r-l+1)
        return ans