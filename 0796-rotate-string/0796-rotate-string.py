class Solution(object):
    def rotateString(self, s, goal):
        n = 0
        for ch in s:
            n += 1

        m = 0
        for ch in goal:
            m += 1

        if n != m:
            return False

        # n rotations check 
        for i in range(n):

            # current s ko goal se compare
            same = True

            for j in range(n):
                if s[j] != goal[j]:
                    same = False
                    break

            if same:
                return True

            # left rotation
            temp = ""

            for j in range(1, n):
                temp += s[j]

            temp += s[0]

            s = temp

        return False