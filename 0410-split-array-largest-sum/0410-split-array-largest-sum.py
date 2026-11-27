class Solution:
    def splitArray(self, nums, k):
        low = max(nums)
        high = sum(nums)

        while low < high:
            mid = (low + high) // 2
            parts = 1
            total = 0

            for num in nums:
                if total + num > mid:
                    parts += 1
                    total = 0

                total += num

            if parts <= k:
                high = mid
            else:
                low = mid + 1

        return low
        