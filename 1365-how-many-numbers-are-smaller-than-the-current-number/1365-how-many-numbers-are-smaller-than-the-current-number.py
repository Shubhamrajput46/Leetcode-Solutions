class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        smaller=[]
        for i in nums:
            count=0
            for j in nums:
                if j<i:
                    count +=1
            smaller.append(count)
        return smaller
        