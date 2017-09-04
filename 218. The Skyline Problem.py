class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        events = sorted([(l,-h,r) for l,r,h in buildings] + list({(r, 0, None) for _,r,_ in buildings}))
        res = [[0,0]]
        hp = [(0,float('inf'))]
        for x, h, r in events:
            while x >= hp[0][1]:
                heapq.heappop(hp)
            if h:
                heapq.heappush(hp,(h,r))
            if res[-1][1] + hp[0][0]!=0: 
                res += ([x, -hp[0][0]],)
        return res[1:]