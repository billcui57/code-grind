class Solution:
    def minDeletions(self, s: str) -> int:

        freq = dict()
        for c in s:
            if c not in freq:
                freq[c] = 1
            else:
                freq[c] += 1
        
        freqVals = freq.values()

        changes = 0
        seenFreqVals = set()

        for val in freqVals:
            _val = val
            while _val in seenFreqVals and _val != 0:
                _val -= 1
                changes += 1
            seenFreqVals.add(_val)
        return changes

            
