class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        dq = collections.deque()
        visited = {word:False for word in wordList}
        dq.append((beginWord,1))
        while dq:
            curr,length = dq.popleft()
            if curr == endWord:
                return length
            for word in wordList:
                if self.diff(curr,word) and visited[word] == False:
                    visited[word] = True
                    dq.append((word,length+1))
        return 0
            
    def diff(self,a,b):
        return sum([1 for (x,y) in zip(a,b) if x!=y]) == 1
            
# 上面是第一版，时间复杂度太高，因为wordList里有巨量单词，每次都遍历时间成本太高。
# 下面的时间复杂度事26*L*N
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        dq = collections.deque()
        visited = {word:False for word in wordList}
        dq.append((beginWord,1))
        while dq:
            curr,length = dq.popleft()
            if curr == endWord:
                return length
            dic = self.nextwords(curr)
            for word in dic:
                if word in wordList and visited[word] == False:
                    visited[word] = True
                    dq.append((word,length+1))
        return 0
            
    def nextwords(self,a):
        return [a[:i] + x + a[i+1:] for x in string.ascii_lowercase for i in range(len(a))]