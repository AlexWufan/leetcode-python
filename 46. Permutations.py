class Solution(object):
#     def permute(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         res = []
#         self.dfs(res, nums, [])
#         return res

#     def dfs(self, res, nums, path):
#         if len(path) == len(nums):
#             res.append(path)
#             return
#         for i in nums:
#             if i in path:
#                 continue
#             self.dfs(res, nums, path+[i])

# # use library
# def permute(self, nums):
#     return list(itertools.permutations(nums))

# iterative

    def permute(self, nums):
        perms = [[]]   
        for n in nums:
            new_perms = []
            for perm in perms:
                for i in range(len(perm)+1):   
                    new_perms.append(perm[:i] + [n] + perm[i:])   ###insert n
            perms = new_perms
            print(perms)
        return perms

if __name__=='__main__':
    asolution = Solution()
    print(asolution.permute([1,2,3]))