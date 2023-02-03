class Solution:
    def minSteps(self, s: str, t: str) -> int:

        delta = {}
        for c in s:
            if c not in delta:
                delta[c] = 1
            else:
                delta[c] += 1
        for c in t:
            if c not in delta:
                delta[c] = -1
            else:
                delta[c] -=1
        print(delta)
        result = 0
        for values in delta.values():
            result+=abs(values)
        
        return result//2
        

