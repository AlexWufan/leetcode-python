class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
	    """
        dic = {}
        res = []
        h = []
        for i in range(len(people)):
        	if people[i][0] in dic:
        		dic[people[i][0]] += (people[i][1],i),
        	else:
        		dic[people[i][0]] = [(people[i][1],i)]
        		h.append(people[i][0])
        h.sort(reverse = True)
        print(dic)


        for height in h:
            dic[height].sort()
            print(dic[height])
            for p in dic[height]:
                res.insert(p[0], people[p[1]])
        return res
################ 下面解法更快###############
        res = []
        for p in sorted(people, key=lambda x: (-x[0], x[1])):
            res.insert(p[1],p)
        return res



if __name__=='__main__':
    asolution = Solution()
    print(asolution.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))