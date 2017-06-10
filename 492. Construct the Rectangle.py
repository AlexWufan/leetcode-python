class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        w = int(area**(0.5))
        while area%w:
            w-=1
        l = area/w
        return [l,w]