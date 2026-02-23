class Solution:
    def totalFruit(self, a: List[int]) -> int:
        n =len(a)
        l = 0
        ans = 0
        d ={}
        for r in range(n):
            d[a[r]] = d.get(a[r],0)+1
            while len(d) > 2:
                d[a[l]]-=1
                if d[a[l]] == 0:
                    del d[a[l]]
                l+=1
            ans=max(ans,r-l+1)
            
        return ans

        