class Solution(object):
    def reverseParentheses(self, s):
        stack = []
        current = ""

        for ch in s:

            if ch == "(":
                # Current string ko stack me save karo
                stack.append(current)

                # Naya substring start karo
                current = ""

            elif ch == ")":
                # Current substring reverse karo
                current = current[::-1]

                # Previous string nikalo
                previous = stack.pop()

                # Dono ko join karo
                current = previous + current

            else:
                # Normal character
                current += ch

        return current
        