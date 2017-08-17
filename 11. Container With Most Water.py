class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height)-1
        v = 0
        while l<r:
            if min(height[l], height[r]) * (r-l) > v:
                v = min(height[l],height[r]) * (r-l)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return v