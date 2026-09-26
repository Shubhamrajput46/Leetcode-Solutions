class Solution(object):
    def evaluate(self, s, knowledge):
        knowledge_dict = dict(knowledge)

        result = []
        i = 0

        while i < len(s):
            if s[i] == '(':
                i += 1
                key = ""

                while s[i] != ')':
                    key += s[i]
                    i += 1

                if key in knowledge_dict:
                    result.append(knowledge_dict[key])
                else:
                    result.append("?")

                i += 1

            else:
                result.append(s[i])
                i += 1

        return "".join(result)