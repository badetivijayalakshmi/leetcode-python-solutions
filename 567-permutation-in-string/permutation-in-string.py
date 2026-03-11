from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        res = []
        count = Counter(s1)
        window = Counter()

        k = len(s1)

        for i in range(len(s2)):
            window[s2[i]] += 1

            if i >= k:
                if window[s2[i-k]] == 1:
                    del window[s2[i-k]]
                else:
                    window[s2[i-k]] -= 1

            if window == count:
                return True
        return False