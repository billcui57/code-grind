# Design A Leaderboard

## Link

https://leetcode.com/problems/design-a-leaderboard/description/

## Where

Leetcode

## Difficulty

Medium

## Description

Design a Leaderboard class, which has 3 functions:

addScore(playerId, score): Update the leaderboard by adding score to the given player's score. If there is no player with such id in the leaderboard, add him to the leaderboard with the given score.
top(K): Return the score sum of the top K players.
reset(playerId): Reset the score of the player with the given id to 0 (in other words erase it from the leaderboard). It is guaranteed that the player was added to the leaderboard before calling this function.
Initially, the leaderboard is empty.

## Solution Main Idea

Use sorteddict or heap


## Code

```python
from sortedcontainers import SortedDict
class Leaderboard:

    def __init__(self):
        self.sortedScore = SortedDict()
        self.scores = dict()
        
        

    def addScore(self, playerId: int, score: int) -> None:
        oldScore = None
        if playerId not in self.scores:
            newScore = score
            self.scores[playerId] = score
        else:
            oldScore = self.scores[playerId]
            newScore = self.scores[playerId] + score
            self.scores[playerId] = newScore
        
        if oldScore is not None:
            self.sortedScore[oldScore] -=1

        if newScore in self.sortedScore:
            self.sortedScore[newScore] +=1
        else:
            self.sortedScore[newScore] = 1

        


    def top(self, K: int) -> int:
        result = 0
        count = 0
        for score,freq in reversed(self.sortedScore.items()):
            if count == K:
                break
            add_count = min(K-count, freq)
            count += add_count
            result += add_count * score
        
        return result

            

        

    def reset(self, playerId: int) -> None:
        oldScore = self.scores[playerId]
        newScore = 0
        self.scores[playerId] = 0

        self.sortedScore[oldScore] -=1

        if newScore in self.sortedScore:
            self.sortedScore[newScore] +=1
        else:
            self.sortedScore[newScore] = 1

        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
```
