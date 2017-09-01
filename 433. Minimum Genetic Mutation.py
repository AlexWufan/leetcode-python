class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        res = []
        self.bfs(start, end, bank, res, 0, [])
        return min(res) if res else -1
    
    def bfs(self, start, end, bank, res, mutation, visited):
        if end == start:
            res.append(mutation)
            return
        for x in bank:
            if self.diff(x,start) and x not in visited:
                visited.append(x)
                mutation+=1
                self.bfs(x, end, bank, res, mutation, visited)
                visited.pop()
                mutation-=1
                
    
    def diff(self, a, b):
        return len(['!' for a,b in zip(a,b) if a!=b ]) == 1