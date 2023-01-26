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