class Solution(object):
    def maxSum(self, nums, k):
        MOD = 10**9 + 7
        bits = [0] * 32

        # Har bit ki frequency count
        for num in nums:
            for i in range(32):
                if num & (1 << i):
                    bits[i] += 1

        ans = 0

        # K maximum numbers construct
        for i in range(k):
            num = 0

            for j in range(32):
                if bits[j] > 0:
                    num |= (1 << j)
                    bits[j] -= 1

            ans = (ans + num * num) % MOD

        return ans