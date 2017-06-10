class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dict = {k:v for v,k in enumerate(list1)}
        minSum = float('inf')
        res = []
        
        for i in range(len(list2)):
            j = dict.get(list2[i],-1)
            if j!=-1 and i+j<= minSum:
                if i+j < minSum:
                    res = []
                    minSum = i+j
                res+=[list2[i]]
                
        return res