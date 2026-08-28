class Solution(object):
    def twoSum(self, nums, target):

        seen = {}

        for i in range(len(nums)):

            required = target - nums[i]

            if required in seen:
                return [seen[required], i]

            seen[nums[i]] = i