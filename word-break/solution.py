class Solution:

    def prefixHasMatch(self, s: str, wordDict):

        matchingWords = []

        for word in wordDict:
            if s.find(word) == 0:
                matchingWords.append(word)

        return matchingWords

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        A = [False] * (len(s) + 1)

        A[len(s)] = True

        for i in reversed(range(len(s) + 1)):
            matchingPrefixes = self.prefixHasMatch(s[i:], wordDict)
            for matchingPrefix in matchingPrefixes:
                A[i] = A[i+len(matchingPrefix)] or A[i]

        return A[0]


class Solution:

    def prefixHasMatch(self, s: str, wordDict):

        matchingWords = []

        for word in wordDict:
            if s.find(word) == 0:
                matchingWords.append(word)

        return matchingWords

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        queue = []
        visited = set()

        queue.append(s)

        while len(queue) > 0:
            node = queue.pop()

            visited.add(node)

            matchingPrefixes = self.prefixHasMatch(node, wordDict)

            for matchedPrefix in matchingPrefixes:
                suffix = node[len(matchedPrefix):]

                if suffix == "":
                    return True

                if suffix not in visited:
                    queue.append(suffix)

        return False
