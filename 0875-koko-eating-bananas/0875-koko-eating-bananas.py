class Solution(object):
    def grtHours(self , piles , mid):
        ans=0
        for pile in piles:
            ans +=(pile + mid -1)//mid
        return ans

    def minEatingSpeed(self, piles, h):
        n=len(piles)

        l=1
        r=max(piles)
        k=r

        while l<=r:
            mid = (l+r)//2
            if self.grtHours(piles,mid)>h:
                l =mid+1
            else:
                k=mid
                r=mid-1   
        return k
        