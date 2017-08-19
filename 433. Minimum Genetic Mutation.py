class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        dic = ['A','C','G','T']
        stack = [start]
        res = []
        visited = []
        mutation = [0]
        self.bfs(start, end, bank, stack, res, mutation, visited, dic)
        return min(res) if res else -1
    
    def bfs(self, start, end, bank, stack, res, mutation, visited, dic):
        if end == start:
            res.append(mutation[0])
            print(res)
            return
        for x in bank:
            if self.diff(x,start) and x not in visited:
                visited.append(x)
                mutation[0]+=1
                self.bfs(x, end, bank, stack, res, mutation, visited, dic)
                visited.pop()
                mutation[0]-=1
                
    
    def diff(self, a, b):
        count = 0
        for x,y in zip(a,b):
            if x!=y:
                count += 1
        return count == 1 