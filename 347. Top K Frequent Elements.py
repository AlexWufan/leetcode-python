class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        for x in nums:
            d[x] = d.get(x, 0) + 1
        bucket = [[] for _ in range(len(nums)+1)]
        for key in d:
            bucket[d[key]].append(key)
        res = []
        for i in range(len(nums),0,-1):
            if bucket[i]:
                res += bucket[i]
        return res[:k]
            
        
        
        
        # return zip(*collections.Counter(nums).most_common(k))[0]

        # return zip(*collections.Counter(nums).most_common(k))[0]
        # return [i[0] for i in collections.Counter(nums).most_commen(k)]

if __name__=='__main__':
    asolution = Solution()
    print(asolution.topKFrequent([1,1,1,2,2,3], 2))