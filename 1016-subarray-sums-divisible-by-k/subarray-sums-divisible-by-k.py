class Solution:
    def subarraysDivByK(self, nums, k):
        mp = {0: 1}   # remainder 0 seen once
        current_sum = 0
        count = 0

        for num in nums:
            current_sum += num
            
            # handle negative remainders safely
            remainder = (current_sum % k + k) % k
            
            # check if same remainder seen before
            if remainder in mp:
                count += mp[remainder]
            
            # update hashmap
            mp[remainder] = mp.get(remainder, 0) + 1

        return count