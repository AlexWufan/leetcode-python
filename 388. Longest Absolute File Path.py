class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        path, maxLen = [], 0
        for s in input.split('\n'):
            path[s.count('\t'):] = [len(s.strip('\t'))]
            maxLen = max(maxLen, sum(path)+len(path)-1 if '.' in s else 0)
        return maxLen


class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        maxlen = 0
        pathlen = {0: 0}
        for line in input.splitlines():
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            if '.' in name:
                maxlen = max(maxlen, pathlen[depth] + len(name))
            else:
                pathlen[depth+1] = pathlen[depth] + len(name) + 1
        return maxlen