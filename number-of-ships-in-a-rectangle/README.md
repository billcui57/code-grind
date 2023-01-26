# Number of Ships in a Rectangle

## Link

https://leetcode.com/problems/number-of-ships-in-a-rectangle/description/

## Where

Leetcode

## Difficulty

Hard

## Description

(This problem is an interactive problem.)

Each ship is located at an integer point on the sea represented by a cartesian plane, and each integer point may contain at most 1 ship.

You have a function Sea.hasShips(topRight, bottomLeft) which takes two points as arguments and returns true If there is at least one ship in the rectangle represented by the two points, including on the boundary.

Given two points: the top right and bottom left corners of a rectangle, return the number of ships present in that rectangle. It is guaranteed that there are at most 10 ships in that rectangle.

Submissions making more than 400 calls to hasShips will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.

## Solution Main Idea

Split into 4 quadrants. Divide and conquer on each.
We can satisfy constraint because at each level there can only be at most 10 subrectangles with ships. And for each of them we can split at most 4 times. There are log10 1000000 = 10 levels. So at most 10 x 10 x 4 = 400 calls to API
