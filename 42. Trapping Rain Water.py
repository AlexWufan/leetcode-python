class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        left, right = 0, len(height) -1
        leftmax = 0
        rightmax = 0
        while left<=right:
            if height[left]<=height[right]:
                if height[left] < leftmax:
                    res += leftmax - height[left]
                else:
                    leftmax = height[left]
                left += 1
            else:
                if height[right] < rightmax:
                    res += rightmax - height[right]
                else:
                    rightmax = height[right]
                right -= 1
        return res