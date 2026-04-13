class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix = { 0 : 1 }
        curr = res = 0
        for num in nums:
            if num % 2 == 1:
                curr += 1
            if curr - k in prefix:
                res += prefix[curr - k]
            prefix[curr] = prefix.get(curr, 0) + 1
        return res
            
        