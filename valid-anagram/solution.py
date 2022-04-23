class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        sFreqDict = dict()

        for sChar in s:
            if sChar in sFreqDict:
                sFreqDict[sChar] += 1
            else:
                sFreqDict[sChar] = 1

        for tChar in t:
            if tChar in sFreqDict:
                sFreqDict[tChar] -= 1
            else:
                return False

        for freq in sFreqDict:
            if sFreqDict[freq] != 0:
                return False

        return True
