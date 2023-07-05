class Solution:
    def average(self, salary: List[int]) -> float:

        cumSum = 0
        maxSal = 0
        minSal = inf

        for sal in salary:
            cumSum += sal
            maxSal = max(maxSal,sal)
            minSal = min(minSal, sal)
        

        return (cumSum-maxSal-minSal)/(len(salary)-2)