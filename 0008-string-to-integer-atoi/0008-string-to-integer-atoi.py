class Solution:
    def myAtoi(self, s):
        i = 0
        n = len(s)

        # 1. Leading spaces skip karo
        while i < n and s[i] == ' ':
            i += 1

        # 2. Sign check karo
        sign = 1
        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            i += 1

        # 3. Digits read karo
        num = 0
        while i < n and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        num *= sign

        # 4. 32-bit integer range check
        num = max(-2**31, min(num, 2**31 - 1))

        return num
        