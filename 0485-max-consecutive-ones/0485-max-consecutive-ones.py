class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count=0
        maximum=0
        for i in range(len(nums)):
            if nums[i]==1:
                count +=1
            else:
                count=0
            maximum=max(maximum,count)
        return maximum
        