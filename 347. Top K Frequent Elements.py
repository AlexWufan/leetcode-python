import collections
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
        return sorted(d.keys(), key=lambda x: d[x], reverse=True)[0:k]

        # return zip(*collections.Counter(nums).most_common(k))[0]
        # return [i[0] for i in collections.Counter(nums).most_commen(k)]

if __name__=='__main__':
    asolution = Solution()
    print(asolution.topKFrequent([1,1,1,2,2,3], 2))