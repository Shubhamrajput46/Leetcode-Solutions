class Solution(object):
    def search(self, nums, target):
        n=len(nums)

        l=0
        r=n-1

        while l<=r:

            mid=(l+r)//2
            if target ==nums[mid]:  
                return mid
            elif target > nums[mid]:
                l=mid+1
            else:
                r=mid-1

        return -1
        