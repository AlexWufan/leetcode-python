class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        output = []
        tmp = []
        for i in range(1, numRows+1):
        	# 每次生成导致很慢
        	new = [1] * i

        	for j in range(1,i-1):
        		new[j] = tmp[j-1]+ tmp[j]
        	tmp = new

        	output.append(new)

        return output

if __name__ == '__main__':
	aSolution = Solution()
	print(aSolution.generate(5))


# 蠢了。一晚上就写了个垃圾，下面是比我好的
class Solution(object):
    def generate(self, numRows):
        res = [[1]]
        for i in range(1, numRows): res.append([1] + [res[i-1][j] + res[i-1][j-1] for j in range(1, i)] + [1])
        return res if numRows else []

class Solution(object):
def generate(self, numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    n,b,res=0,[1],[]
    while n<numRows:
        res.append(b)
        b=[1]+[b[i]+b[i+1] for i in range(len(b)-1)]+[1]
        n+=1
    return res

# recursive
def generate(self, numRows):
        res = [[1]]
        for i in range(1, numRows):
            res += [map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1])]
        return res[:numRows]