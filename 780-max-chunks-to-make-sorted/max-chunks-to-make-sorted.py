class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks, cur_max = 0, -inf
        for i, num in enumerate(arr):
            cur_max = max(cur_max, num)
            if cur_max == i:
                chunks += 1
        return chunks