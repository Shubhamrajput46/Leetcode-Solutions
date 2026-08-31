class Solution:
    def nodesBetweenCriticalPoints(self, head):
        critical = []

        prev = head
        curr = head.next
        pos = 1

        while curr.next:
            if ((curr.val > prev.val and curr.val > curr.next.val) or
                (curr.val < prev.val and curr.val < curr.next.val)):

                critical.append(pos)

            prev = curr
            curr = curr.next
            pos += 1

        # Less than 2 critical points
        if len(critical) < 2:
            return [-1, -1]

        # Minimum distance between adjacent critical points
        minDistance = float('inf')

        for i in range(1, len(critical)):
            minDistance = min(
                minDistance,
                critical[i] - critical[i - 1]
            )

        # Maximum distance = last - first
        maxDistance = critical[-1] - critical[0]

        return [minDistance, maxDistance]