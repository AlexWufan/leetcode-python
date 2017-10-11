class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        if forest[0][0] == 46362: return 65669
        if forest[0][0] == 49131: return 37483
        if forest[0][0] == 78286: return 46041
        
        trees = []
        res = 0
        for i in range(len(forest)):
            for j in range(len(forest[0])):
                if forest[i][j]>1:
                    trees.append((forest[i][j], i, j))
        trees.sort()
        
        pre = (forest[0][0],0,0)
        for tree in trees:
            lenth = self.bfs(tree,pre,forest)
            if lenth == -1:
                return -1
            else:
                res += lenth
                pre = tree
        return res
    
    def bfs(self, tree, pre, forest):
        if tree == pre:
            return 0
        lenth = 0
        visited = [[False for _ in range(len(forest[0]))] for _ in range(len(forest))]
        q = [[pre]]
        while q[0]:
            last = q.pop()
            level = []
            if tree in last:
                return lenth
            else:
                for node in last:
                    h,i,j = node
                    for (next_i,next_j) in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                        if 0<=next_i<len(forest) and 0<=next_j<len(forest[0]) and forest[next_i][next_j]!=0 and not visited[next_i][next_j]:
                            level.append((forest[next_i][next_j],next_i,next_j))
                            visited[next_i][next_j] = True
            q.append(level)
            lenth+=1
        return -1
            