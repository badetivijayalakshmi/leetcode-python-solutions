class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l = 0
        prefix = {0:1}
        count = 0
        ans = 0
        for num in nums:
            if num % 2 == 1:
                count+=1
            if (count-k) in prefix:
                ans += prefix[count-k]
                
            prefix[count] = prefix.get(count,0)+1
        return ans
            
        