class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        jobs = sorted(zip(endTime, startTime, profit))
        A = [0] * len(jobs)
        A[0] = jobs[0][2]

        for i in range(1, len(jobs)):
            e, s, p = jobs[i]
            justBefore = (
                bisect.bisect_right(jobs, s, hi=i, key=lambda a: a[0]) - 1
            )  # binary search on jobs to find last index of s, minus 1 to get the last element before s
            if justBefore == -1:
                A[i] = max(A[i - 1], p)
            else:
                A[i] = max(A[i - 1], p + A[justBefore])
        return A[-1]
