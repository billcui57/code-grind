class Solution:
    def maxValue(self, n: str, x: int) -> str:
        result = None
        isNegative = False
        i = 0
        while i < len(n):
            if n[i] == "-":
                isNegative = True
                i+=1
                continue
            if isNegative:
                if x >= int(n[i]):
                    i+=1
                    continue
            else:
                if x <= int(n[i]):
                    i+=1
                    continue
            break
        result = n[:i] + str(x) + n[i:]
        return result