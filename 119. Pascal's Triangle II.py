# class Solution(object):
#     def getRow(self, rowIndex):
#         """
#         :type numRows: int
#         :rtype: List[List[int]]
#         """
#         row = [1]
#         for i in range(1,rowIndex+1):
#         	row = [1]+[ row[j-1] + row[j] for j in range(1, i)]+[1]
#         return row


# 更smart的方法

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        row = [1]
        for i in range(rowIndex):
        	# row = [x+y for x,y in zip([0]+row,row+[0])]
        	row = list(map(lambda x,y: x+y, [0]+row,row+[0]))
        return row




if __name__ == '__main__':
	aSolution = Solution()
	print(aSolution.getRow(3))

