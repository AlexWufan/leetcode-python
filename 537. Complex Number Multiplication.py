class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        p = int(a.split('+')[0]) *int(b.split('+')[0])- int(a.split('+')[1][:-1])*int(b.split('+')[1][:-1])
        q = int(a.split('+')[1][:-1])*int(b.split('+')[0]) + int(b.split('+')[1][:-1])*int(a.split('+')[0])
        res = str(p) + '+' + str(q) + 'i'
        return res