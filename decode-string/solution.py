class Solution:
    def decodeString(self, s: str) -> str:
        s = list(s)

        stack = []

        i = 0
        number=""

        result = ""
        while i < len(s):
            if s[i].isnumeric():
                number += s[i]
            elif s[i] == "[":
                stack.append([int(number),""])
                number =""
            elif s[i] == "]":
                freq,part = stack.pop()
                if len(stack) > 0:
                    stack[-1][1] += part * freq
                else:
                    result += part * freq
            else:
                if len(stack) > 0:
                    stack[-1][1] += s[i]
                else:
                    result += s[i]
            i += 1
        return result
        




























