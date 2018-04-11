class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        def area(point):
            x,y,z = point
            return 0.5*abs((y[0]-x[0])*(z[1]-y[1]) + (z[0]-y[0])*(x[1]-z[1]) + (z[0]-y[0])*(z[1]-y[1]))
        return max(map(area,itertools.combinations(points,3)))