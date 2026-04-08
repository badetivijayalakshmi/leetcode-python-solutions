class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr = res = 0
        prefixSum = { 0 : 1 }
        for n in nums:
            curr += n
            if curr - k in prefixSum:
                res += prefixSum[curr - k]
            prefixSum[curr] = 1 + prefixSum.get(curr,0)
        return res