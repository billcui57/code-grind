class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        head = 0
        tail = 0
        seen = set()

        maxLength = 0

        while head < len(s):
            if s[head] not in seen:
                seen.add(s[head])
                maxLength = max(head - tail + 1, maxLength)
                head += 1
            else:
                # keep removing until we remove the repeating char
                seen.remove(s[tail])
                tail += 1

        return maxLength


# or (better)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = dict()

        lo = 0
        hi = 0

        s= list(s)

        best = 0
        while hi < len(s):
            # maintain invariant that s[lo:hi] contains no repeating characters 
            if s[hi] in seen:
                seenIndex = seen[s[hi]]
                for i in range(lo, seenIndex+1):
                    seen.pop(s[i])
                lo = seenIndex+1
            seen[s[hi]] = hi

            best = max(hi-lo+1, best)

            hi+=1
        return best


