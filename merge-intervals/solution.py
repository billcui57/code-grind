class Solution:

    def is_overlapping(self,a, b):
        return not ((a[1] < b[0]) or (b[1] < a[0]))

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = list(sorted(intervals, key= lambda x: x[0]))
        merged = []

        for interval in intervals:
            if len(merged) == 0:
                merged.append(interval)
                continue
            last = merged.pop()
            if self.is_overlapping(interval, last):
                new_interval = [min(interval[0], last[0]), max(interval[1],last[1])]
                merged.append(new_interval)
            else:
                merged.append(last)
                merged.append(interval)
        return merged