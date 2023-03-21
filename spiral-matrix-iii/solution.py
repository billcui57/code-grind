class Solution:

    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        # step increases by 1 after every 2 direction moves

        rLoc = rStart
        cLoc= cStart
        stepVal = 1


        def getDelta():
            i = 0
            while True:
                if i== 0:
                    yield (0, 1)
                elif i==1:
                    yield (1 ,0)
                elif i==2:
                    yield (0, -1)
                else:
                    yield (-1, 0)
                i = (i+1)%4

        getDeltaGen = getDelta()
        result = []
        result.append([rLoc, cLoc])

        for i in range(2 * max(rows,cols)):
            for dirMove in range(2):
                rDelta, cDelta = next(getDeltaGen)
                for step in range(stepVal):
                    rLoc += rDelta
                    cLoc += cDelta
                    if rLoc < rows and cLoc < cols and rLoc > -1 and cLoc > -1:
                        result.append([rLoc, cLoc])
            stepVal +=1
        return result
