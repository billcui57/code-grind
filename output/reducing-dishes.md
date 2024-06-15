# Reducing Dishes

## Link
https://leetcode.com/problems/reducing-dishes/description/

## Where
Leetcode

## Difficulty
Hard

## Description
A chef has collected data on the satisfaction level of his n dishes. Chef can cook any dish in 1 unit of time.

Like-time coefficient of a dish is defined as the time taken to cook that dish including previous dishes multiplied by its satisfaction level i.e. time[i] * satisfaction[i].

Return the maximum sum of like-time coefficient that the chef can obtain after dishes preparation.

Dishes can be prepared in any order and the chef can discard some dishes to get this maximum value.


## Solution Main Idea
Sort the array and reverse it.
Notice that by adding an element we can increase the previous result as we are "shifting" it.
The array being sorted and reversed gives the best chance as we can greedily go through it.

Use DP as well to store prev results.
Recurrence relation:
e.g going from -1,0,5 -> -8,-1,0,5
        # accum1 = -1*1 + 0*2 + 5*3, accum2 = -1+0+5
        # newaccum1 = -8*1 + -1*2 + 0*3 + 5*4
        # = -8*1 + -1 + -1*1 + 0 + 0*2 + 5 + 5*3
        # = -8*1 + -1 + 0 + 5 + -1*1 + 0*2 + 5*3
        # = -8*1 + accum2 + accum1
        # newaccum2 = -8 + accum2
 

## Code

```python
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


        
```
