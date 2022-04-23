class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        freqDict = {}
        head = 0
        tail = 0
        s = list(s)
        longestLength = 0
        mostFreqLetter = None

        while head < len(s):
            if s[head] in freqDict:
                freqDict[s[head]] += 1
            else:
                freqDict[s[head]] = 1

            mostFreqLetter = (
                s[head]
                if not mostFreqLetter or freqDict[s[head]] > freqDict[mostFreqLetter]
                else mostFreqLetter
            )

            highestFreq = freqDict[mostFreqLetter]

            neededChanges = (head - tail + 1) - highestFreq

            if neededChanges <= k:
                longestLength = max(longestLength, head - tail + 1)
            else:
                freqDict[s[tail]] -= 1
                tail += 1
            head += 1
        return longestLength
