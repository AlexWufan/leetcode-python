class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        for i in range(len(flowerbed)):
            if (i == 0 or not flowerbed[i-1]) and not flowerbed[i] and (i == len(flowerbed)-1 or not flowerbed[i+1] ):
                count += 1
                flowerbed[i] = 1
        return count >= n