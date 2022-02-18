class Solution:

    def inSeen(self, array, seen):

        if array[0] in seen:
            if array[1] in seen[array[0]]:
                if array[2] in seen[array[0]][array[1]]:
                    return True

        return False

    def addSeen(self, array, seen):

        if self.inSeen(array, seen):
            return

        if array[0] not in seen:
            seen[array[0]] = {}

        if array[1] not in seen[array[0]]:
            seen[array[0]][array[1]] = {}

        if array[2] not in seen[array[0]][array[1]]:
            seen[array[0]][array[1]][array[2]] = True

    def twoSum(self, nums, target, start, seen):

        store = {}

        for i in range(start, len(nums)):
            store[nums[i]] = i

        result = []

        for i in range(start, len(nums)):
            if (target - nums[i] in store) and (store[target-nums[i]] > i):

                thing = [-1 * target, nums[i], target-nums[i]]

                if not self.inSeen(thing, seen):

                    self.addSeen(thing, seen)

                    result.append(thing)

        return result

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        seen = {}

        nums = sorted(nums)

        result = []

        for i in range(len(nums)):

            target = 0-nums[i]

            twoSumResults = self.twoSum(nums, target, i+1, seen)

            result += twoSumResults

        return result
