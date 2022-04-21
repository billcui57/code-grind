class Solution:

    brackMap = {"(": ")", "[": "]", "{": "}"}

    def isValid(self, s: str) -> bool:

        openStack = []

        for i in range(len(s)):
            if s[i] in self.brackMap:
                openStack.append(s[i])
            else:
                if len(openStack) > 0 and self.brackMap[openStack[-1]] == s[i]:
                    openStack.pop()
                else:
                    return False
        return len(openStack) == 0
