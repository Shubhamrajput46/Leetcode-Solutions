class Solution(object):
    def isIsomorphic(self, s, t):

         # length check
        n = 0
        for ch in s:
            n += 1

        m = 0
        for ch in t:
            m += 1

        if n != m:
            return False

        mapST = {}
        mapTS = {}

        for i in range(n):

            a = s[i]
            b = t[i]

            # s -> t mapping check
            if a in mapST:
                if mapST[a] != b:
                    return False

            # t -> s mapping check
            if b in mapTS:
                if mapTS[b] != a:
                    return False

            mapST[a] = b
            mapTS[b] = a

        return True