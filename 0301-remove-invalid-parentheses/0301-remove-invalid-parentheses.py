class Solution:
    def removeInvalidParentheses(self, s):
        def is_valid(string):
            count = 0

            for ch in string:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1

                    if count < 0:
                        return False

            return count == 0

        queue = [s]
        visited = {s}

        while queue:
            next_level = []

            for current in queue:

                if is_valid(current):
                    return [
                        x for x in visited
                        if is_valid(x) and len(x) == len(current)
                    ]

                for i in range(len(current)):
                    if current[i] not in "()":
                        continue

                    new_string = current[:i] + current[i + 1:]

                    if new_string not in visited:
                        visited.add(new_string)
                        next_level.append(new_string)

            queue = next_level

        return [""]