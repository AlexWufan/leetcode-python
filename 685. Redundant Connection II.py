class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        def find(x):
            return x if g[x] == x else find(g[x])
        if not edges:
            return []
        g = {k:k for k in range(1,len(edges)+1)}
        
        candidate1, candidate2 = [-1,-1], [-1,-1]
        for edge in edges:
            if g[edge[1]] != edge[1]:
                candidate1 = [g[edge[1]], edge[1]]
                candidate2 = [edge[0], edge[1]]
            else:
                g[edge[1]] = edge[0]
        print(candidate1,candidate2)
        
        g = {k:k for k in range(1,len(edges)+1)}
        for edge in edges:
            if edge == candidate2:
                continue
            x, y = edge[0], edge[1]
            x_parent = find(x)
            y_parent = find(y)
            print(x_parent, y_parent)
            if x_parent == y_parent:
                if candidate1[0] == -1:
                    return edge
                return candidate1
            g[y_parent] = x_parent
        return candidate2
    
        
        

if __name__=='__main__':
    asolution = Solution()
    print(asolution.findRedundantDirectedConnection([[1,2],[2,3],[3,4],[4,1],[1,5]]))
