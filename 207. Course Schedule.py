class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        indegree = [[] for _ in range(numCourses)]
        outdegree = [0 for _ in range(numCourses)]
        
        for p in prerequisites:
            indegree[p[1]].append(p[0])
            outdegree[p[0]] += 1
        dq = []
        for i in range(numCourses):
            if outdegree[i] == 0:
                dq.append(i)
        count = 0
        while dq:
            x = dq.pop(0)
            count += 1
            for i in indegree[x]:
                outdegree[i] -= 1
                if outdegree[i] == 0:
                    dq.append(i)
        return count == numCourses
            