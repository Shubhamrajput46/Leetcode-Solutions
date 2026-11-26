class Solution:
    def shipWithinDays(self, weights, days):
        low = max(weights)
        high = sum(weights)

        while low < high:
            mid = (low + high) // 2
            total = 0
            count = 1

            for weight in weights:
                if total + weight > mid:
                    count += 1
                    total = 0

                total += weight

            if count <= days:
                high = mid
            else:
                low = mid + 1

        return low
        