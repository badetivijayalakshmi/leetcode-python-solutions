class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = {0:1}
        total = count = 0

        for n in nums:
            total += n

            if total - k in mp:
                count += mp[total - k]

            mp[total] = 1 + mp.get(total,0)
        
        return count
        