class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for point in points:
            dict = {}
            for dot in points:
                distance = (dot[0]-point[0])**2 + (dot[1]-point[1])**2
                dict[distance] = 1 + dict.get(distance, 0)
            for num in dict:
                res += dict[num]*(dict[num]-1)
        return res