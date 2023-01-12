from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:

        wordFreq = Counter(s)
        length = 0
        usedMiddle = False

        for letter, freq in wordFreq.items():
            canUse = (freq // 2) * 2
            length += canUse
            remaining = max(0, freq - canUse)
            if remaining > 0 and usedMiddle is False:
                length += 1
                usedMiddle = True

        return length
