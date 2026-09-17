class Solution:
    def minSumOfLengths(self, arr, target):
        INF = float('inf')

        n = len(arr)

        # dp[i] = minimum length of a valid subarray
        # ending at or before index i
        dp = [INF] * n

        left = 0
        curr_sum = 0

        answer = INF

        for right in range(n):
            curr_sum += arr[right]

            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            if curr_sum == target:
                length = right - left + 1

                # Previous non-overlapping subarray
                if left > 0 and dp[left - 1] != INF:
                    answer = min(
                        answer,
                        length + dp[left - 1]
                    )

                # Best single subarray till right
                if right == 0:
                    dp[right] = length
                else:
                    dp[right] = min(dp[right - 1], length)

            else:
                if right > 0:
                    dp[right] = dp[right - 1]

        return -1 if answer == INF else answer