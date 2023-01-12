class Solution:
    def twoSum(self, start, nums, target):
        seen = set()
        result = []
        
        for i in range(start, len(nums)):
            if target - nums[i] in seen:
                result.append((nums[i], target-nums[i]))
            seen.add(nums[i])
        return result
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        #invariant of solution: a[i] <= a[j] <= a[k]

        result = set()

        for i in range(len(nums)):
            twoSumResults = self.twoSum(i+1, nums, -1 * nums[i])
            for a,b in twoSumResults:
                result.add((a,b,nums[i]))
        
        return [[a,b,c] for a,b,c in list(result)]
                





