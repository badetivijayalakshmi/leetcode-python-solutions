class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        temp = 0
        ans = 0
        for i in range(len(cost)-1, -1, -1):
            if temp == 2:
                temp = 0
            else:
                ans += cost[i]
                temp += 1
        return ans