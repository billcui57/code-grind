class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:

        # -9,-8,-1,0,5

        # accum1 = -1*1 + 0*2 + 5*3, accum2 = -1+0+5
        # newaccum1 = -8*1 + -1*2 + 0*3 + 5*4
        # = -8*1 + -1 + -1*1 + 0 + 0*2 + 5 + 5*3
        # = -8*1 + -1 + 0 + 5 + -1*1 + 0*2 + 5*3
        # = -8*1 + accum2 + accum1
        # newaccum2 = -8 + accum2

        satisfaction = list(reversed(sorted(satisfaction)))

        accum1 = 0
        accum2 = 0
        for sat in satisfaction:
            newaccum1 = sat + accum2 + accum1
            newaccum2 = accum2 + sat
            if newaccum1 < accum1:
                return accum1
            accum1 = newaccum1
            accum2 = newaccum2
        return accum1


        