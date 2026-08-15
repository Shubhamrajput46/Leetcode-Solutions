class Solution(object):
    def longestSubsequence(self, nums):
        xor = 0

        for x in nums:
            xor ^= x

        if xor != 0:
            return len(nums)

        return len(nums) - 1 if any(nums) else 0
        