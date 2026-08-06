class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maxCand=max(candies)
        ans=[]
        for i  in candies:
            if (i + extraCandies)>=maxCand:
                ans.append(True)
            else:
                ans.append(False)
        return ans
        