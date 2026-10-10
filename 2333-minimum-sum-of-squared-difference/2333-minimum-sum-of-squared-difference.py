class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        n = len(nums1)
        k = k1 + k2
        diff = []

        total = 0
        for i in range(n):
            d = nums1[i] - nums2[i]
            if d < 0:
                d = -d
            diff.append(d)
            total += d

        if total <= k:
            return 0

        left = 0
        right = 0

        for d in diff:
            if d > right:
                right = d

        while left < right:
            mid = (left + right) // 2
            needed = 0

            for d in diff:
                if d > mid:
                    needed += d - mid

            if needed <= k:
                right = mid
            else:
                left = mid + 1

        level = left
        ans = 0
        remaining = k

        for d in diff:
            if d > level:
                remaining -= d - level
                d = level
            ans += d * d

        # Jo operations bach gaye, unse level wale differences
        # ko ek-ek karke level - 1 kar  hain.
        for d in diff:
            if remaining == 0:
                break
            if d >= level and level > 0:
                ans -= level * level
                ans += (level - 1) * (level - 1)
                remaining -= 1

        return ans