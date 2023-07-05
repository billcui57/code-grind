class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        nums1Set = set(nums1)
        nums2Set = set(nums2)

        answer2 = set()
        answer1 = set()

        for num in nums1:
            if num not in nums2Set:
                answer1.add(num)
        for num in nums2:
            if num not in nums1Set:
                answer2.add(num)
        return [list(answer1), list(answer2)]
