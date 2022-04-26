class Solution:

    # local longest palindrome finder, rooted at s[left:right+1]
    def helper(self, s, left, right):

        while left - 1 >= 0 and right + 1 < len(s):

            if s[left - 1] == s[right + 1]:
                left -= 1
                right += 1
            else:
                return s[left : right + 1]

        return s[left : right + 1]

    def longestPalindrome(self, s: str) -> str:

        longestAbs = ""

        for i in range(len(s)):
            longestLocal = ""

            # if applicable, also include palindromes rooted at s[i:i+1]
            if i + 1 < len(s) and s[i] == s[i + 1]:
                longestLocal = self.helper(s, i, i + 1)
                longestAbs = (
                    longestLocal if len(longestLocal) > len(longestAbs) else longestAbs
                )

            longestLocal = self.helper(s, i, i)

            longestAbs = (
                longestLocal if len(longestLocal) > len(longestAbs) else longestAbs
            )

        return longestAbs
