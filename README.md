####刷题笔记
#记录一点点刷题细节

##11.2
- 66题，可以用字符串，也可以先用`x*10+y`算成数字再处理，值得一提的是在
	```
	reduce(lambda x,y: x*10+y, digits)
	```
	中是选digits中第一第二个元素，再开始迭代第三个第四个
	
	`reduce`在3.0中被转移了需要重新引入
	```
	from functools import reduce
	```
##11.1
- 118和119题，杨辉三角，需要判断好边界值，119用O(k) space,在一行上面迭代

##10.31

- 169题，摩尔投票 Moore voting algorithm,原理进出栈,只需要O(1)空间  
比哈希表省空间
- 121题，动态规划， kadane algorithm 时间复杂度O(n)

##10.30
- 189题，inplace修改数组，如果`nums = ...`就是创建新数组，如果`nums[:]`就是在原来数组修改

##10.29
-414题，heapq 可以用来做topk，O(n)时间
- heapq 并不是以大小排序的。heap[0]代表最小,  
heapq.heappushpop() 先push再pop一气呵成 速度快

- `cmp`在3.0中被移除了，比如这个比较大小的 
	```
	nums.sort(cmp= lambda a, b: -1 if b == 0 else 0)
	```

- 排序时间复杂度 `O(lgn)`， python内置的`sorted`是timesort ，很高级，虽然复杂度是 `O(lgn)`

##10.28
- 438题，用sliding window,用固定长度的字典，然后往后移动

##之前的记不清哪天了
- 204题，找质数，512曾经的考试题 = =，很蠢的做法是对每一个数，判断是否是质数，用循环循环到n^1/2, 更巧妙的办法就是从开头开始把235...的倍数都标记成非质数，时间复杂度大大降低，