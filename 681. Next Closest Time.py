class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        number_set = set(time)
        current = 60 * int(time[:2]) + int(time[3:])
        res = set()
        while True:
            current = (current + 1) % (24 * 60)
            new_time = '%02d:%02d' % divmod(current,60) 
            res = set(new_time)
            if res <= number_set:
                return new_time