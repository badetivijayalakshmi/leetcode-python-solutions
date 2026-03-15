from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count = Counter(p)
        window = Counter()
        res = []
        k = len(p)
        for i in range(len(s)):
            window[s[i]] += 1
            if i >= k:
                window[s[i-k]] -= 1
                if window[s[i-k]] == 0:
                    del window[s[i-k]]
            if window == count:
                res.append(i-k+1)
        return res   

        