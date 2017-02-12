class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return []
        dic = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        res = []
        self.dfs(dic, digits, 0, '', res)
        print(res)
        return res

    def dfs(self, dic, digits, index, path, res):
    	if index == len(digits):
    		res.append(path)
    		return
    	for i in dic[digits[index]]:
    		self.dfs(dic, digits, index+1, path+i, res)
if __name__ == '__main__':
	aSolution = Solution()
	aSolution.letterCombinations('23')