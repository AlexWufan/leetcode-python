from collections import deque
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        indegree = [[] for _ in range(numCourses)]
        outdegree = [0 for _ in range(numCourses)]
        dq = deque()
        for p in prerequisites:
            outdegree[p[0]]+=1
            indegree[p[1]].append(p[0])
        for i in range(numCourses):
            if outdegree[i] == 0:
                dq.append(i)
        k = 0
        res = []
        while dq:
            x = dq.popleft()
            res.append(x)
            k += 1
            for i in indegree[x]:
                outdegree[i] -= 1
                if outdegree[i] == 0:
                    dq.append(i)
        return res if k== numCourses else []