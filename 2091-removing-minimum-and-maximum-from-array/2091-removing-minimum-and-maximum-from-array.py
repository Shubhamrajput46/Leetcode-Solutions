class Solution(object):
    def minimumDeletions(self, nums):
        n = len(nums)

        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))

        left = min(min_index, max_index)
        right = max(min_index, max_index)

        # Case 1: Remove both from front
        front = right + 1

        # Case 2: Remove both from back
        back = n - left

        # Case 3: One from front, one from back
        both = (left + 1) + (n - right)

        return min(front, back, both)
        