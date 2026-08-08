class Solution(object):
    def intersection(self, nums1, nums2):
        intersection = list(set(nums1) & set(nums2))
        return intersection
        