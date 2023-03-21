class Solution:
    def minOperations(self, s: str) -> int:
        #01
        numChanges = 0

        for i in range(len(s)):
            if int(s[i]) != i%2:
                numChanges += 1
        
        return min(numChanges, len(s)-numChanges)