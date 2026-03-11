class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hashmap = defaultdict(int)
        sL = len(s)
        pL = len(p)
        res = []
        if pL > sL:
            return []
        for ch in p:
            hashmap[ch] +=1
        for i in range(pL-1):
            if s[i] in hashmap:
                hashmap[s[i]] -= 1
        for i in range(-1,sL-pL+1):
            if i > -1 and s[i] in hashmap:
                hashmap[s[i]] += 1
            if i+pL < sL and s[i+pL] in hashmap:
                hashmap[s[i+pL]] -= 1
            if all(v == 0 for v in hashmap.values()):#anagram check
                res.append(i+1)
        return res   

        