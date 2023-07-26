from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # go from the top

        minClimbingCosts = [0] * (len(cost)+1) # top floor is 1 above ladder
        # can start at 0 or 1
        minClimbingCosts[0] = 0
        minClimbingCosts[1] = 0

        for i in range(len(cost) + 1):
            if i==1 or i==0:
                continue
            climb1Cost = minClimbingCosts[i-1] + cost[i-1]
            climb2Cost = minClimbingCosts[i-2] + cost[i-2]
            minToStepCost = min(climb2Cost, climb1Cost)
            minClimbingCosts[i] = minToStepCost

        return minClimbingCosts[-1]

