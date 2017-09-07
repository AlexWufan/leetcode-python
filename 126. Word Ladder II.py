# 先做BFS,记录父节点，然后进行DFS。
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        paths = collections.defaultdict(set)
        wordList = set(wordList)

        queue = collections.deque([(beginWord, 1)])
        while queue:
            word, dist = queue.popleft()
            for i in range(len(word)):
                for letter in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = word[:i]+letter+word[i+1:]
                    if newWord in wordList:
                        if newWord in dic and dic[newWord] < dist+1:
                            continue
                        if newWord not in dic:
                            queue.append((newWord, dist+1))
                        dic[newWord] = dist+1
                        paths[newWord].add(word)
                        if newWord == endWord:
                            continue

        #print paths
        return [path[::-1] for path in getPaths(beginWord, endWord, paths)]

def getPaths(beginWord, endWord, paths):
    if beginWord == endWord:
        return [[beginWord]]
    res = []
    for word in paths[endWord]:
        for path in getPaths(beginWord, word, paths):
            res.append([endWord]+path)
    return res

# 记录父节点，反向查找
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordList = set(wordList)
        level = {beginWord}
        parents = collections.defaultdict(set)
        while level and endWord not in parents:
            next_level = collections.defaultdict(set)
            for node in level:
                for x in string.ascii_lowercase:
                    for i in range(len(node)):
                        n = node[:i]+x+node[i+1:]
                        if n in wordList and n not in parents:
                            next_level[n].add(node)
            level = next_level
            parents.update(next_level)
        res = [[endWord]]
        print(parents)
        while res and res[0][0]!=beginWord:
            res = [[p]+r for r in res for p in parents[r[0]]]
        return res

# 建立图，然后bfs
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordList = set(wordList)
        wordList.add(beginWord)
        # wordList.add(endWord)
        edge = {word:[] for word in wordList}
        for word in wordList:
            words = self.nextwords(word)
            for x in words:
                if x in wordList:
                    edge[word].append(x)
                    
        q = collections.deque([[beginWord]])
        visited = set([beginWord])
        res = []
        flag = False
    
        while not flag and q:
                allword=[]
                for _ in range(len(q)):
                    curPath = q.popleft()
                    cur=curPath[-1]
                    for i in edge[cur]:
                        if i==endWord:
                            res.append(curPath+[endWord])
                            flag=True
                        if i not in visited:
                            q.append(curPath+[i])
                            allword.append(i)
                visited |= set(allword)
        return res
                        
            
    def nextwords(self,a):
        return [a[:i] + x + a[i+1:] for x in string.ascii_lowercase for i in range(len(a)) if x!=a[i]]



# 下面的解法是TLE，backtracking.
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        res = []
        wordList = set(wordList)
        visited = {word:False for word in wordList}
        length = self.ladderLength(beginWord, endWord,wordList)
        if length == 0:
            return []
        
        self.backtrack(beginWord, endWord, wordList, res, [beginWord], visited, length)
        return res
            
    def nextwords(self,a):
        return [a[:i] + x + a[i+1:] for x in string.ascii_lowercase for i in range(len(a))]
    
    def backtrack(self, start, end, wordList, res, path, visited, length):
        if start == end and len(path) == length:
            res.append(path)
            return
        dic = self.nextwords(start)
        for word in dic:
            if word in wordList and visited[word] == False:
                if len(path) >= length:
                    break
                visited[word] = True
                self.backtrack(word, end, wordList, res, path+[word],visited, length)
                visited[word] = False
                
    def ladderLength(self, beginWord, endWord, wordList):
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