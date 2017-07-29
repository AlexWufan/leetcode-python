class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters.sort()
        houses.sort()
        i, distance = 0, 0
        for house in houses:
            while i < len(heaters)-1 and abs(heaters[i] - house) >= abs(heaters[i+1] - house):
                i += 1
            distance = max(distance, abs(heaters[i]- house))
        return distance