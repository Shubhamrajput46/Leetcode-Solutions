from collections import Counter

class Solution:
    def largestOverlap(self, img1, img2):
        n = len(img1)

        points1 = []
        points2 = []

        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    points1.append((i, j))

                if img2[i][j] == 1:
                    points2.append((i, j))

        count = Counter()

        for x1, y1 in points1:
            for x2, y2 in points2:
                dx = x2 - x1
                dy = y2 - y1

                count[(dx, dy)] += 1

        return max(count.values()) if count else 0