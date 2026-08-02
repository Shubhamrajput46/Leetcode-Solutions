class Solution:
    def reverse(self, x):

        rev = 0

        while x != 0:

            if x < 0:
                digit = -(abs(x) % 10)
            else:
                digit = x % 10

            if rev > 214748364 or (rev == 214748364 and digit > 7):
                return 0

            if rev < -214748364 or (rev == -214748364 and digit < -8):
                return 0

            rev = rev * 10 + digit

            # Python me integer division negative numbers ke liye alag behave karti hai
            if x < 0:
                x = -(-x // 10)
            else:
                x = x // 10

        return rev
        