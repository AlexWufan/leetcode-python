####刷题笔记
#记录一些刷题细节，很惭愧只做了一点微小的工作

##11.8
- 113题，可以用DFS，判断是否和为sum，然后就加入res，或者用递归，这题以后再看下，其中有些`path`如何存储的不太明白，是复制了无数个`path`数组来存储吗，在不同的层，如果不符合就return了None，这个应该是深层复制，有空请教一下大腿。ps. 递归的时候是由下向上的，一层层的下去，再一层层地返回
- 437题，可以用递归写出O(n)时间复杂度的算法，但是还是不知道O(n)的怎么写。

##11.7
- 98题，验证是否是二叉搜索树，二叉搜索树左子树永远比右子树小，而且左右子树都是二叉搜索树，这题关键在于传递参数，来记录祖父节点的值。所以定义两个变量，每迭代一次更新一次,实现约束条件。也可以用中序遍历，然后判断数组是否是递增的。树的中序遍历：
	```
    def inOrder(self, root, output):
	    if root is None:
	        return
	    
	    self.inOrder(root.left, output)
	    output.append(root.val)
	    self.inOrder(root.right, output)
    ```
把中间的处理步骤写在前面就是前序，写在后面就是后序，非常简单。

##11.6
- 447，104，100这三题都是树，都是树的遍历，可以用递归，DFS或者BFS写。
- 112题，递归
- 257题，用递归可以写，也可以用DFS or BFS 写，path保存路径，要对每一个节点单独用一个path记录路径，所以用list或者tuple来匹配节点和他的单独路径。

##11.5
- 287题，用二分法，时间复杂度O(nlgn)，另外有O(n)复杂度的算法，用快慢指针寻找环,要推导一些边界值，代码不是很复杂。
- 168和171题，同一个问题，168注意字母的临界值，用ascii码匹配
- 4题，回忆求一个array的中位数用divide and conquer 可以在linear time 解决，具体就是分三段，小于，等于，大于，然后递归(算法概论）。这题是求两个sorted的array的中位数，可以利用sorted的这个性质来减小时间复杂度，达到O(log(m+n))。具体是:把`nums1`和`nums2`都割成两半，比较A和B前一半最后一个值大小，较小的那个不可能包含我们要找的k值，所以缩减了A的一半大小，然后递归。原理就是这样，要注意很多边界值。

##11.4
- 229题，还是Moore voting algorithm，用两个容器存candidate，迭代的时候注意不能让同样的值被两个容器同时出现，同样的candidate要在一个容器
- 167题，two sum II,用哈希表没什么好说的，或者头尾指针往中间找(题目说拍好序的)，或者还可以用二分查找。时间复杂度O(nlgn)

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
- 在python的文档中写道，如果要在迭代的时候修改迭代对象，最好copy一个在新的上操作，因为如果删除元素的时候下一次迭代可能会跳过下一个迭代对象，插入同理，会导致一些nasty bugs

- 283题和27题，差不多的题目，一个需要保持顺序一个不用，27题把当前迭代`nums[i]=nums[n-1]`，不断用最后一个来替换，然后`n-1`, 只需要迭代k次，缺点是不能保持顺序，283题要求保持顺序，那就只能交换了

##11.1
- 118和119题，杨辉三角，需要判断好边界值，119用O(k) space,在一行上面迭代

##10.31

- 169题，摩尔投票 Moore voting algorithm,原理进出栈,只需要O(1)空间  
比哈希表省空间
- 121题，动态规划， kadane algorithm 时间复杂度O(n)

##10.30
- 189题，inplace修改数组，如果`nums = ...`就是创建新数组，如果`nums[:]`就是在原来数组修改

##10.29
- 414题，heapq 可以用来做topk，O(n)时间
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
- 204题，找质数，512曾经的考试题 = =，很蠢的做法是对每一个数，判断是否是质数，用循环循环到n^1/2, 更巧妙的办法就是从开头开始把235...的倍数都标记成非质数，时间复杂度大大降低