class Solution:
    def resultArray(self, nums, k):
        result = [0] * k
        dp = [0] * k

        for num in nums:
            new_dp = [0] * k

            # Start a new subarray from current element
            r = num % k
            new_dp[r] += 1

            # Extend previous subarrays
            for old_r in range(k):
                if dp[old_r]:
                    new_r = (old_r * num) % k
                    new_dp[new_r] += dp[old_r]

            dp = new_dp

            # Add all subarrays ending here to answer
            for r in range(k):
                result[r] += dp[r]

        return result