class Solution:
    def is_overlap(self, interval, newInterval):
        return not (interval[0] > newInterval[1] or interval[1] < newInterval[0])

    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:

        if len(intervals) == 0:
            return [newInterval]
        if newInterval[1] < intervals[0][0]:
            intervals.insert(0, newInterval)
            return intervals
        if intervals[-1][1] < newInterval[0]:
            intervals.append(newInterval)
            return intervals

        result = []
        start = None
        end = None
        mergeMode = False

        for i in range(len(intervals)):
            if not mergeMode:
                if self.is_overlap(intervals[i], newInterval):
                    mergeMode = True
                    start = min(intervals[i][0], newInterval[0])
                else:
                    if (
                        i > 0
                        and intervals[i - 1][1] < newInterval[0]
                        and newInterval[1] < intervals[i][0]
                    ):
                        result.append(newInterval)
                    result.append(intervals[i])
            else:
                if not self.is_overlap(intervals[i], newInterval):
                    mergeMode = False
                    end = max(newInterval[1], intervals[i - 1][1])
                    result.append([start, end])
                    result.append(intervals[i])

        if mergeMode:
            result.append([start, max(intervals[-1][1], newInterval[1])])

        return result
