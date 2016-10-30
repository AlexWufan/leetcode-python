# 1
# class Solution(object):
#     def intersect(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: List[int]
#         """
#         dict1 = {}
#         result = []
#         for x in nums1:
#         	if x in dict1:
#         		dict1[x] += 1
#         	else:
#         		dict1[x] = 1

#         for x in nums2:
#         	if x in dict1 and dic1[x]>0:
#         		dict1[x] -= 1
#         		result.append(x)

#         return result


# 2
# import collections
# counter1 = collections.Counter(nums1)
# counter2 = collections.Counter(nums2)
# return list((counter1 & counter2).elements())

from collections import Counter as ct
class Solution(object):
    def intersect(self, nums1, nums2):
        c3 = ct(nums1)&ct(nums2)
        print(c3, ct(nums1),ct(nums2))
        ret = []
        for ch in c3:
            ret += ([ch]*c3[ch])
        return ret    

if __name__=='__main__':
    asolution = Solution()
    print(asolution.intersect([1,2,2,1], [2, 2]))