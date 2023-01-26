class Solution:

    def removeDuplicates(self, s: str, k: int) -> str:

        stack = []

        for char in s:
            if len(stack) > 0 and char == stack[-1][0]:
                stack[-1][1] += 1
            else:
                stack.append([char,1])
                
            if len(stack) > 0 and stack[-1][1] == k:
                stack.pop()
        return "".join([x[0]*x[1] for x in stack])