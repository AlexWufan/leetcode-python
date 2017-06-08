class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        self.dfs(res,nums,[],0)
        return res

    def dfs(self, res, nums, path, index):
        res.append(path)
        for i in range(index, len(nums)):
            self.dfs(res, nums, path+[nums[i]], i+1)


# one line, from discuss
def subsets(self, nums):
    return reduce(lambda L, ele: L + [l + [ele] for l in L], nums, [[]])

def subsets(self, nums):
    [[x for x in l if x is not None] for l in itertools.product(*zip(nums, [None] * len(nums)))]

def subsets(self, nums):
    [l for n in range(len(nums) + 1) for l in itertools.combinations(nums, n)]

# Iteratively
    def subsets(self, nums):
        res = [[]]
        for num in sorted(nums):
            res += [item+[num] for item in res]
            print(res)
        return res


    # Bit Manipulation    
def subsets2(self, nums):
    res = []
    for i in range(1<<len(nums)):
        tmp = []
        for j in range(len(nums)):
            if i>>j & 1:
                tmp.append(nums[j])
        res.append(tmp)
    return res

if __name__=='__main__':
    asolution = Solution()
    print(asolution.subsets([1,2,3]))


