class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:

        last_seen_colour = colors[0]
        last_seen_index = 0

        cost = 0

        for i in range(1,len(colors)):
            if colors[i] == last_seen_colour:
                if neededTime[i] > neededTime[last_seen_index]:
                    cost += neededTime[last_seen_index]
                    last_seen_colour = colors[i]
                    last_seen_index = i
                else:
                    cost += neededTime[i]
            else:
                last_seen_colour = colors[i]
                last_seen_index = i
        return cost
                    
                    

