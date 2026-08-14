class Solution(object):
    def lowerbound(self, nums, target):
        n=len(nums)
        l=0
        r=n-1
        ans=n

        while l<=r:
            mid=(l+r)//2

            if nums[mid]>=target:
                ans=mid
                r=mid-1
            else:
                l=mid+1

        return ans

    def uperbound(self, nums, target):
        n=len(nums)
        l=0
        r=n-1
        ans=n

        while l<=r:
            mid=(l+r)//2

            if nums[mid]>target:
                ans=mid
                r=mid-1
            else:
                l=mid+1

        return ans

    def searchRange(self, nums, target):
        lb=self.lowerbound(nums,target)
        ub=self.uperbound(nums,target)

        if lb==ub:
            return [-1,-1]
        else:
            return [lb,ub-1]
        