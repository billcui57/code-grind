class Solution:
    def bt(self, numFreq):

        chosen = set()

        result = []

        for num in numFreq:
            if num not in chosen and numFreq[num] > 0:
                numFreq[num] -= 1
                rests = self.bt(numFreq)
                for rest in rests:
                    rest.append(num)
                    result.append(rest)
                if len(rests) == 0:
                    result.append([num])
                numFreq[num] += 1
        return result

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        numFreq = {}

        for num in nums:

            if num not in numFreq:
                numFreq[num] = 1
            else:
                numFreq[num] += 1

        return self.bt(numFreq)


#         [1,1,2] 1 [1,2] 11[2] 112
#                         12[1] 121
#                 #1 was just chosen so dont choose it

#                 2 [1,1] 21[1] 211
#                         #1 was just chosen so dont choose it
