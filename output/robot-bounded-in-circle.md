# Robot Bounded In Circle

## Link

https://leetcode.com/problems/robot-bounded-in-circle/

## Where

Leetcode

## Difficulty

Medium

## Description

On an infinite plane, a robot initially stands at (0, 0) and faces north. Note that:

The north direction is the positive direction of the y-axis.
The south direction is the negative direction of the y-axis.
The east direction is the positive direction of the x-axis.
The west direction is the negative direction of the x-axis.
The robot can receive one of three instructions:

"G": go straight 1 unit.
"L": turn 90 degrees to the left (i.e., anti-clockwise direction).
"R": turn 90 degrees to the right (i.e., clockwise direction).
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

## Solution Main Idea

Determine if the total displacement is 0 after four cycles of instructions.


## Code

```python
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

```
