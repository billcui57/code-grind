class Solution:

    def prefixHasMatch(self, s, mapping):

        matches = []

        for i in range(len(s)):
            if s[0:i+1] in mapping:
                matches.append(s[0:i+1])

        return matches

    def numDecodings(self, s: str) -> int:

        mapping = set([str(i) for i in range(1, 27)])

        A = [0] * (len(s) + 1)

        A[len(s)] = 1

        for i in reversed(range(len(s))):
            matches = self.prefixHasMatch(s[i:], mapping)
            A[i] = 0
            for match in matches:
                A[i] += A[i + len(match)]

        return A[0]
