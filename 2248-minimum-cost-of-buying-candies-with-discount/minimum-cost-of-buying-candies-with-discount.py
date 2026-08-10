class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        n = len(cost)
        # [2,2,5,6,7,9]
        ans = 0
        took = 0
        for i in range(n-1,-1,-1):
            # print(cost[i]+cost[i-1])
            if took == 2:
                took = 0
            else:
                ans = ans + cost[i]
                took=took+1
            
        return ans