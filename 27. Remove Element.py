class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # 使用指针，把同样的元素移到了后面，然后切片，两个指针循环次数最大达到2n
        p = 0
        for i in range(len(nums)):
        	if nums[i] != val:
        		nums[i], nums[p] = nums[p], nums[i]
        		p += 1
        

        return len(nums[:p])

if __name__ == '__main__':
	aSolution  = Solution()
	print(aSolution.removeElement([3,2,2,3,3,3,3],3))




# 另外一种写法，循环次数等于元素的个数
        n = len(nums) 
        while i < n:
        	if nums[i] == val:
        		nums[i] = nums[n-1]
        		n -= 1
        	else:
        		i += 1
        return n


# 更简洁，35ms
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        while (nums.count(val)!=0):
            nums.remove(val)
        
        return len(nums)