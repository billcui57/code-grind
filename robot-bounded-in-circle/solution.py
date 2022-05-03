class Solution:
    def isRobotBounded(self, instructions: str) -> bool:

        direction = 0  # 0 = north, east = 1, south = 2, west = 3

        northSouthDisplacement = 0
        eastWestDisplacement = 0

        for instr in instructions * 4:
            if instr == "R":
                direction = (direction + 1) % 4

            if instr == "L":
                direction = (direction - 1) % 4

            if instr == "G":
                if direction == 0:
                    northSouthDisplacement += 1
                elif direction == 1:
                    eastWestDisplacement += 1
                elif direction == 2:
                    northSouthDisplacement -= 1
                else:
                    eastWestDisplacement -= 1

        return northSouthDisplacement == 0 and eastWestDisplacement == 0
