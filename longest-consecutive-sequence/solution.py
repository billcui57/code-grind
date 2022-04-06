class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        maxLength = 0

        numSet = set(nums)

        # duplicates dont matter so we ignore it to be faster
        for x in numSet:
            length = 1
            if x-1 not in numSet:
                oneBigger = x + 1
                while oneBigger in numSet:
                    length += 1
                    oneBigger += 1

            maxLength = max(length, maxLength)

        return maxLength
