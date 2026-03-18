class Solution:
    def numberOfSubarrays(self, nums, k):
        
        def atMost(k):
            l = 0
            count = 0
            res = 0
            
            for r in range(len(nums)):
                if nums[r] % 2 == 1:
                    count += 1
                
                while count > k:
                    if nums[l] % 2 == 1:
                        count -= 1
                    l += 1
                
                res += (r - l + 1)
            
            return res
        
        return atMost(k) - atMost(k - 1)