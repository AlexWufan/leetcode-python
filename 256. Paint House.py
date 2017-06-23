class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:return 0
        n = len(costs)
        for i in range(1,n):
            costs[i][0] += min(costs[i-1][1],costs[i-1][2])
            costs[i][1] += min(costs[i-1][0],costs[i-1][2])
            costs[i][2] += min(costs[i-1][0],costs[i-1][1])
        return min(costs[n-1])

def minCost(self, costs):
    prev = [0] * 3
    for now in costs:
        prev = [now[i] + min(prev[:i] + prev[i+1:]) for i in range(3)]
    return min(prev)