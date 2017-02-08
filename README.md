####刷题笔记
#记录一些刷题细节，很惭愧只做了一点微小的工作


##2.8
- 138. Copy List with Random Pointer.![http://images.cnitblog.com/i/627993/201405/221027256064414.jpg)
+ 首先，在原链表的每个节点后面都插入一个新节点，新节点的内容和前面的节点一样。比如上图，1后面插入1，2后面插入2，依次类推。

+ 其次，原链表中的random指针如何映射呢？比如上图中，1节点的random指针指向3，4节点的random指针指向2。如果有一个tmp指针指向1（蓝色），则一条语句：tmp.next.random = tmp.random.next；就可以解决这个问题。

+ 第三步，将新的链表从上图这样的链表中拆分出来。


##2.7
- 387. First Unique Character in a String, Python的解法很简单，过一遍字母表就可以，存储`index`，输出最小的`index`时间复杂度是O(n)。比较好的解是用hash表对每个字符统计出现次数，然后再根据字符串顺序输出次数为1的字符，但是字符串太长，我们要找的字母在字符串最后，就会浪费很多效率，所以最优解是在hash存字符出现次数的时候同时存`index`，就可以实现只扫一遍。c++可以用`std::pair`实现。
- 459. Repeated Substring Pattern. Python的做法是把两个`str`连接起来，去头去尾，然后在这个长的链接`str`里面寻找本来的字符串`str`,`find()`方法还能返回`index`. 直接判断可以用`in`，可以做到一行。  
`return str in (str+str)[1:-1]`  
比较一般的做法是KMP算法,时间复杂度应该是O(n)。参见<http://www.ruanyifeng.com/blog/2013/05/Knuth–Morris–Pratt_algorithm.html>. 还可以用试除数的方法，复杂度worst case是O(n^2).
- 155. Min Stack，正常写法，因为要求`getMin()`O(1)的查询速度，所以要牺牲空间来维护最小值，[这里](http://stackoverflow.com/questions/685060/design-a-stack-such-that-getminimum-should-be-o1)说的很清楚，如果`getMin()`是O(1)，那么当`pop()`出去的如果是最小值，那么`pop()`会变成O(n),而且再`push()`的时候也是O(n),如果用tuple(或者另一个ministack)来存储值的话会增加空间。所以基本上都是trade-off. java的写法要使用一个栈的话必须`push`两次，一次记录当前的`min`,一次记录`x`，还可以优化为只有更新`min`的时候才把`min`进栈。


##2.6
- 337题， House Robber III, 还是dp，但这次是树，递归的时候巧妙的使用了一个tuple，来记录前面的最优解。挺难的。要想一会才能明白。[这个解法](https://discuss.leetcode.com/topic/39846/easy-to-understand-java/3)很不错。
- 236题，Lowest Common Ancestor of a Binary Tree,可以用递归来解决，递归寻找两个带查询LCA的节点`p`和`q`，当找到后，返回给它们的父亲。如果某个节点的左右子树分别包括这两个节点，那么这个节点必然是所求的解，返回该节点。否则，返回左或者右子树（哪个包含`p`或者`q`的就返回哪个）。java解法的一个小trick:  
`return left==null? right : right == null? left: root;`
- 20题，Valid Parentheses，用栈，对于前括号一律把对应的后括号进栈，这样实际上字符串里对应的后括号和栈里的是一致的，不一样就返回`False`。java中`stack`是`vector`的延伸，性能上不好，用`deque`来代替`stack`比较好.
- 48题，Rotate Image，先上下交换再沿对角线交换。注意边界值避免重复交换，Python的解法比较多，妙用`zip(*)`可以实现对角线交换。`matrix[:]`可以直接inpalce修改。

##2.5
- 213题，House Robber II, 同样是dp，需要转换成House Robber I来做，因为第一个和最后一个不能同时抢，所以分成两个子问题，一个是`nums[0]~nums[n-2]`,另一个是`nums[1]~nums[n-1]`，然后`max`一下，需要特别注意的就是边界值。

##1.22
- 70题，dp问题，本质是Fibonacci,可以暴力，时间复杂度`2^n`,空间`O(n)`,递归树的深度可以到`n`.也可以动态规划，存一个数组然后更新，`O(n)`space，或者连数组都不用直接三个变量存。最优解是直接用Fibonacci公式，`pow()`方法用`log(n)`时间。
- 198题，House Robber I, 同样是dp问题，需要状态转移方程：`dp[i] = max(dp[i - 1], dp[i - 2] + num[i])`.

##1.17
- 485,487题，weekly contest,比较简单，487可以用一步就可以实现，用两个变量存low位置。

##1.11
- 417题，Pacific Atlantic Water Flow,这题用DFS, 反向从边上往中间迭代，能到达的标记为True,分别维护两个矩阵一个P一个A,最后如果两个矩阵同一个位置都是True那么这个点是。
- 329题，Longest Increasing Path in a Matrix. 这题跟417题很像，对每一个点进行dfs，维护一个cache来记录长度，需要注意的是在dfs这个函数里面的计数，要保证记录最长长度，就要用`max()`函数来维护。这道hard题总的来说还是不难的。
- 101题， Symmetric Tree, 这题用递归，分别验证`root`左右值，然后递归左右节点。或者用`level order traversal`也可以，用`list`和反转之后的`list`比较，或者用`stack`，一次`append`一个`tuple`,验证是否相等或者是否都为空。

##1.7
- 109题，两种方法
 + 第一种是快慢指针，时间复杂度O(nlgn)。用慢指针找到`inorder`的中点，分别对两边进行递归。中间要切断一些边。
 + 第二种是Bottom-up方法，用index来表示中点，一层层递归下去，先选最左边的结点，然后接到root上，然后接上右边的，整个过程是从下往上合并。因为先计算长度size，O(n)时间，然后`inorder reconstruction`,时间O(n)，所以总体时间是O(n). Space 是constant space所以是O(1) space.
- 还有一个大坑是，一不小心就空格和tab混合使用了，这样加注释的时候会产生不一样的注释缩进，导致无法AC！fuck！耽误一小时时间。
- 200题，number of islands，用DFS，把每一个遇到的‘1’(岛)，寻找它相连的其他岛，变为`0`，因为我们把相连的`1`看作一个。时间复杂度O(mn),空间复杂度O(mn),mn为尺寸。
- 394题，Decode String,又有两种做法。这题很有意思，也不太容易。
 1. 第一种双栈，一个记录数字，也就是k，一个记录字符串，每次遇到'['的时候更新数字栈，同时也要压一个空的`''`进字符串栈，然后用`-1`索引来操作栈，最后字符串栈的第一个元素就是完整的字符串。这是比较一般的做法。
 2. 第二种是用`python`的特性，用`stack = [['',]]`这样形式的栈，更新数字的时候，用`stack.append(['', int(num)])`,这样有数字的情况下就会自动嵌套，最后同样输出第一层的第一个元素。

##1.6
- 450题，删除BST的结点。
 + 一种做法是用左孩子的最右边(最大)结点，把右孩子接上去，会增加树的高度，影响查询速度。还可以把左孩子接到右孩子的最左端。一样的。
 + 另外一种做法是吧root替换为右孩子最左边(小)的节点，然后对右孩子递归操作。缺点是有的时候改那么多`val`不如改reference
- 108题，把有序array编程平衡BST，用递归很简单就寻找中位数，找到root，再对左右结点递归操作。
- 114题，Flattern Binary Tree,把BST压平。
 + 第一种做法是用递归，先把左右子树递归压平。再把右子树连接到左子树后面,再把左子树连接到`root.right`,最后把`root.left = None`. 
 + 第二种做法，叫 Morris traversal，非常有趣，做法是把左子树连接到`root.right`，然后找到左子树中最右边的结点，把右子树连接上去，然后再把左子树连接到`root.right`,然后`root = root.right` 一个个循环下去。空间复杂度O(1),时间复杂度O(n).厉害了
- 105和106题，Constuct Binary Tree from Preorder and Inorder/Inorder and Postorder Traversal。这两题[水中的鱼](http://fisherlei.blogspot.com)的文章<http://fisherlei.blogspot.com/2013/01/leetcode-construct-binary-tree-from.html> 有详细的解释。主要原理就是利用前序/后序遍历找到`root`，然后根据`root`分割`inoder`,然后递归左右子树。唯一一点要说的是`Python`写的中间切片操作会生成新的数组，导致MLE或者一些奇怪的bug,所以最好用`self._build_tree(inorder, low_in, high_in, postorder, low_post, high_post)`




##1.5
- 107题，104的变形，倒过来就行了，也可以用栈加level标记高度的方法，速度还是比简单方法慢。
- 110题，Balanced Binary Tree, 用递归写比较容易，求左右树高，绝对值小于1，同时验证左右子树是否是balanced，时间复杂度O(n)。
- 111题，求最短叶子的高度，用递归，对每一层min，如果有左右节点有一个不存在的情况下就max。或者用`level order traversal`,遇到左右两个字节点都是`None`的情况下就可以直接返回树高。

##1.4
- 104题，把树按照高度一层一层输出，ez题，一层层循环更新当层结点就行了。

##12.1
- 230题，寻找二叉搜索树中第k个值，直接用inorder遍历然后存储成数组，然后取出结果。discuss看到有人说的生成器的用法，用`yield`语法

#11.24
- 94题和144题，分别是树的前序遍历和中序遍历，递归很简单。主要用迭代的方法做，用栈，前序遍历简单直接右-左顺序压栈就可以。中序遍历难一点，要先压栈到最左边，然后不断往`node.right`走，如果没有right那么就会pop中间节点，就是我们想要的流程。 
- 145题，后序遍历，两种解决方法：
    1. 第一种双栈，第一个栈做左右交换的前序遍历，也就是说先压`node.left`，再压`node.right`，这样用第二个栈把节点都pop出来就是后序遍历。时间复杂度`O(n)`.
    2. 第二种解法是用pre记录上一个节点，我们使用`prev`变量跟踪上一次访问的节点。假设栈顶元素是`curr`,当`prev`是`curr`的父节点时，我们正在向下遍历树。此时，优先遍历`curr`的左孩子（将左孩子压入栈）。如果没有左孩子，再看右孩子。如果左右孩子都不存在（`curr`是叶节点），就输出`curr`的值并弹出栈顶元素。如果`prev`是`curr`的左孩子，我们正在从左子树向上遍历。我们看一下`curr`的右孩子。如果可以，就从右孩子向下遍历（将右孩子压入栈），否则打印`curr`的值并弹出栈顶元素。如果`prev`是`curr`的右孩子，我们正在从右子树向上遍历。打印`curr`的值并弹出栈顶元素。时间复杂度O(h), h为树高

##11.22
- 235题，注意是二叉搜索树，BST，所以可以用value直接算，写了个栈竟然不对。

##11.20
- 463题，双循环，每一个方块也就是1，加4，每遇到一个邻居-1
- 462题，排序，然后一个循环。时间复杂度O(nlogn),有时间复杂度O(n)的算法，就是求中位数的复杂度。
- 226题，反转二叉树，著名的Max Howell梗。直接交换就行了，然后递归。或者用DFS

##11.17
- 404题，简单的递归或者DFS

##11.8
- 113题，可以用DFS，判断是否和为sum，然后就加入res，或者用递归，在不同的层，如果不符合就return了None，这个应该是深层复制, 递归的时候是由下向上的，一层层的下去，再一层层地返回
- 437题，可以用递归写出O(n)时间复杂度的算法，用哈希表维护一个从root到当前node的路径之和，和有这样路径和的路径个数，然后如果从root到当前node的路径和`so_far - s`存在hashtable里面，那么说明找到了子路径，`res=dic.get(so_far,0)+1`。然后递归。注意在完成一个节点的时候，就在hashtable里面，把root到当前node的路径和个数-1

##11.7
- 98题，验证是否是二叉搜索树，二叉搜索树左子树永远比右子树小，而且左右子树都是二叉搜索树，这题关键在于传递参数，来记录祖父节点的值。所以定义两个变量，每迭代一次更新一次,实现约束条件。也可以用中序遍历，然后判断数组是否是递增的。树的中序遍历：
	```
    def inOrder(self, root, output):
	    if root is None:
	        return None
	    
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