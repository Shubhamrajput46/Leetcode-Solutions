class Solution(object):
    def braceExpansionII(self, expression):
        def multiply(A, B):
            return {a + b for a in A for b in B}

        def parse(i):
            result = set()
            current = {""}

            while i < len(expression) and expression[i] != '}':
                
                if expression[i] == '{':
                    # Parse inside braces
                    inside, i = parse(i + 1)
                    current = multiply(current, inside)

                elif expression[i] == ',':
                    # Union current result
                    result |= current
                    current = {""}
                    i += 1

                else:
                    # Single letter
                    current = multiply(current, {expression[i]})
                    i += 1

            result |= current

            # Skip closing '}'
            if i < len(expression) and expression[i] == '}':
                i += 1

            return result, i

        result, _ = parse(0)

        return sorted(result)
        