class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        l1 = list(map(int, version1.split('.')))
        l2 = list(map(int, version2.split('.')))
        
        for i in range(max(len(l1),len(l2))):           
            v1 = l1[i] if i < len(l1) else 0
            v2 = l2[i] if i < len(l2) else 0
            if v1>v2:
                return 1
            elif v1<v2:
                return -1
        return 0