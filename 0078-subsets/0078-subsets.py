class Solution(object):
    def subsets(self, nums):
        result = []

        def solve(index,current):
            if index==len(nums):
                result.append(current[:])
                return

            # choice 1 current index nhi lete hai
            solve(index+1,current) 

            # choice 2 curret index lete hai
            current.append(nums[index])
            solve(index+1,current)
            current.pop()

        solve(0,[])
        return result       