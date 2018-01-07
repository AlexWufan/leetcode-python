class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        g = {k:k for k in range(1,len(edges)+1)}
        def find(x):
            return x if g[x] == x else find(g[x])
        for e in edges:
            x,y = map(find,e)
            if x == y:
                return e
            g[y] = x