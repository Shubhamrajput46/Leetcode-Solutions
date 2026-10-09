class Solution(object):
    def minInsertions(self, s):
        open_count = 0
        insertions = 0
        i = 0

        while i < len(s):

            if s[i] == '(':
                open_count += 1

            else:
                # Check next character ')' hai ya nahi
                if i + 1 < len(s) and s[i + 1] == ')':
                    i += 1
                else:
                    # Ek closing ')' insert karni padegi
                    insertions += 1

                # Closing pair ke liye opening bracket chahiye
                if open_count > 0:
                    open_count -= 1
                else:
                    # Ek '(' insert karna padega
                    insertions += 1

            i += 1

        # Har remaining '(' ke liye 2 closing brackets chahiye
        insertions += open_count * 2

        return insertions
        