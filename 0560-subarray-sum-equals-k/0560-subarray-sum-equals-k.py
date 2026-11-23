class Solution:
    def subarraySum(self, nums, k):
        freq = {0: 1}
        total = 0
        count = 0

        for num in nums:
            total += num
            need = total - k

            if need in freq:
                count += freq[need]

            if total in freq:
                freq[total] += 1
            else:
                freq[total] = 1

        return count