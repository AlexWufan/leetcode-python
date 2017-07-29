# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        tmp = ['','','','']
        total = 0
        while total < n:
            count = read4(tmp)
            if not count:
                break
            count = min(count, n - total)
            
            for i in range(count):
                buf[total] = tmp[i]
                total += 1
            # buf[total:] = tmp[:count]
            # total += count
        return total