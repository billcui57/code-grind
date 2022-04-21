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
                seen.remove(s[tail])
                tail += 1

        return maxLength
