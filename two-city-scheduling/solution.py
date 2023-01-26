class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        sorted_costs = list(reversed(sorted(costs, key = lambda x: abs(x[1]-x[0]))))
        num_a = 0
        num_b = 0
        total_cost = 0
        for cost in sorted_costs:
            if cost[0] < cost[1]:
                if num_a < len(costs)//2:
                    total_cost += cost[0]
                    num_a += 1
                else:
                    total_cost += cost[1]
                    num_b += 1
            elif cost[1] < cost[0]:
                if num_b < len(costs)//2:
                    total_cost += cost[1]
                    num_b +=1
                else:
                    total_cost += cost[0]
                    num_a +=1
            else:
                if num_a < len(costs)//2:
                    total_cost += cost[0]
                    num_a += 1
                else:
                    total_cost += cost[1]
                    num_b += 1
        return total_cost
                    

                

