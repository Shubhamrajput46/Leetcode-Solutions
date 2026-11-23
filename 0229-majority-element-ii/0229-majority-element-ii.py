class Solution:
    def majorityElement(self, nums):
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        result = []

        for num in freq:
            if freq[num] > len(nums) // 3:
                result.append(num)

        return result