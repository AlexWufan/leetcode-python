class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        return self.dfs(s, wordDict, {})
    
    def dfs(self, s, wordDict,memo):
        if s in memo:
            return memo[s]
        if not s:
            return None
        res = []
        for word in wordDict:
            if s.startswith(word):
                if len(s) == len(word):
                    res.append(word)
                else:
                    for path in self.dfs(s[len(word):],wordDict,memo):
                        path = word +' '+ path
                        res.append(path)
        memo[s] = res
        return res

