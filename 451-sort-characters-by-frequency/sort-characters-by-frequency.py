class Solution:
    def frequencySort(self, s: str) -> str:
        res = []
        freq = Counter(s)

        bucket = [[] for _ in range(len(s)+1)]

        for ch, val in freq.items():
            bucket[val].append(ch)

        for i in range(len(bucket)-1,0,-1):
            for ch in bucket[i]:
                res.append(ch * i)
        return ''.join(res)

        