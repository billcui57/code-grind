class Solution:
    # palindrome finder for palindromes rooted at s[left:right+1]
    def helper(self, s, left, right):

        count = 1

        while left - 1 >= 0 and right + 1 < len(s):
            if s[left - 1] == s[right + 1]:
                left -= 1
                right += 1
                count += 1
            else:
                return count

        return count

    def countSubstrings(self, s: str) -> str:

        counter = 0

        for i in range(len(s)):

            # if applicable, also include palindromes rooted at s[i:i+1]
            if i + 1 < len(s) and s[i] == s[i + 1]:
                counter += self.helper(s, i, i + 1)

            counter += self.helper(s, i, i)

        return counter
