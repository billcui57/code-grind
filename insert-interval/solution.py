class Solution:

    def isOverlapping(self,intervala, intervalb):
        return not (intervala[1] < intervalb[0] or intervala[0] > intervalb[1])

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # degen case: intervals is empty
        if len(intervals) == 0:
            return [newInterval]

        # case 1: newInterval appears before intervals
        if newInterval[1] < intervals[0][0]:
            intervals.insert(0, newInterval)
            return intervals
        
        # case 2: newInterval appears after intervals
        if newInterval[0] > intervals[-1][1]:
            intervals.append(newInterval)
            return intervals

        result = []
        mergeMode = False
        mergeIntervalStart = 0
        mergeIntervalEnd = 0
        # case 3: 
        for i in range(len(intervals)):
            if self.isOverlapping(intervals[i], newInterval):
                if mergeMode is True:
                    continue
                else:
                    mergeIntervalStart = min(intervals[i][0], newInterval[0])
                    mergeMode = True
            else:
                if mergeMode is True:
                    mergeIntervalEnd = max(intervals[i-1][1], newInterval[1])
                    result.append([mergeIntervalStart, mergeIntervalEnd])
                    mergeMode = False
                else:
                    if (
                        i > 0
                        and intervals[i - 1][1] < newInterval[0]
                        and newInterval[1] < intervals[i][0]
                    ):
                        result.append(newInterval)
                result.append(intervals[i])
        if mergeMode is True:
            mergeIntervalEnd = max(intervals[-1][1], newInterval[1])
            result.append([mergeIntervalStart, mergeIntervalEnd])
        return result

