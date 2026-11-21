class Solution(object):
    def rearrangeArray(self, nums):
        positive=[]
        negative=[]

        for num in nums:
            if num>0:
                positive.append(num)
            else:
                negative.append(num)

        result=[]
        for i in range(len(positive)):
            result.append(positive[i])
            result.append(negative[i])
            
        return result

        