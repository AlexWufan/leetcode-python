###  刷题笔记
# 记录一些刷题细节，很惭愧只做了一点微小的工作

## 9.28
- 435题. Non-overlapping Intervals.贪心算法，按照`i.end`排序，越早结束的 越不影响后面的。出现overlap，那么`count+=1`，如果没有 更新`i.end`.
- 418题. Sentence Screen Fitting. 这一题预处理字符串，把每个单词之间用空格' '串起来，然后再在后面加一个空格' ', 这样就可以利用一个游标，来计算一共走的步数，除以字符串的长度就能计算出来多少遍。具体操作是:
  每一层(row)start游标+cols，这是这一轮可用的所有步长
  `if s[start % len] == ' '`这个位置，也就是下一行起始位，是空格' '，说明上一行刚好装了完整的单词，没有出现撕裂，那么因为根据规则要去这个空格，但是我们处理字符串的时候加了一个空格，所以我们要start+1，把这个算进去，为了计算正确的times.
  `else:`说明这个开头是落在了字母上，
    if `s[(start-1) % l]`这个位置的字母，是空格' '，说明刚好上一行最后一个位置里是空格符' ',皆大欢喜，什么都不用做。
    如果不是，那么我们要退格子，因为有单词撕裂了。用一个循环，`while s[(start-1)%l] != ' ': start -= 1`, 把上一行撕裂的单词的部分往后移动，这样会出现很多空格，但实际上并没有算在有效步长里，所以要`start-=1`来补偿回去。
最后，拿`start // l`即可得出使用sentence的次数。

## 9.25
- 23题. Merge k Sorted Lists.用heapq，时间复杂度O(nlgn).或者用priority queue.

## 9.24
- 682题. Baseball Game. 用一个数组计算每一轮的得分，求和即可。
- 42题. Trapping Rain Water.从两边开始，分别维护一个左边最大和一个右边最大，如果小于那么就可以存水，如果大于就更新左右最大值。就好比中间有一片战争迷雾，如果只发现右边高一点，我们认为整体水面高度是和左边一样高，慢慢往中间推移。和第11题有异曲同工之处。

## 9.23
- 680题. Valid Palindrome II. 暴力的解法是一个一个试验，时间`O(n^2)`空间`O(n)`.更好的解法，先开始从头i尾j开始比较，发现不同`s[i]!=s[j]`，那么就判断`s[i],s[i+1]...s[j]`即`s[i:j]`和`s[i+1]....s[j+1]`即`s[i+1:j+1]`.时间`O(n)`空间`O(1)`.
- 674题. Longest Continuous Increasing Subsequence.一次循环即可，每次循环记录最长长度。

## 9.12
- 146题. LRU Cache.要维护一个常用的cache，不常用的要被慢慢弹出。用OrderedDict可以解决。
- 42题. Trapping Rain Water. 


## 9.9
- 540题. Single Element in a Sorted Array. 二分法，要讨论mid的奇偶。更好的做法是，永远把mid设置为最中间的数偏左一位，永远为偶数，维持r-l+1也就是数组长度为奇数，就可以不用讨论，而且更好理解。
- 22题. Generate Parentheses. dfs解决。典型题。
- 153题. Find Minimum in Rotated Sorted Array.典型的二分查找，注意的是如果是比较`l`和`mid`，需要考虑如果是完全有序的，那么就直接返回最左边。如果直接`mid`跟`r`比，就不用，因为`mid`会一直往左边缩。

## 9.8
- 139题. Word Break. `Dp`可以解决，dp数组里存的`d[i]`，`s[:i+1]`是否可以word break，还可以用bfs。初始dp[0]为`True`.
- 140题. Word Break II. dfs递归，这里的`res`是在函数内部，每次递归之后都会合并到上一层，最后组成完整的`res`。注意边界。关键点是，使用一个`memo`dict，来存储已经出现过的`s`的`res`，这样可以节约大量时间，因为比如像`aaaaaaa`这种，就会产生大量的冗余计算.

## 9.7
- 671题. Second Minimum Node In a Binary Tree.因为不能算重复元素，所以用set()来存结果，跑一边dfs把所有值加进去，排序输出第二个即可。
- 50题. Pow(x, n). 直接循环实现会越界，这题可以用递归，也可以用迭代。

## 9.6
- 127题. Word Ladder. 经典的`bfs`，需要注意时间复杂度，用单向`bfs`的复杂度是`26*L*N`.要把`list`改成`set`，因为`list`的`in`操作是`O(n)`而`set`的是`O(1)`. 还可以用双向bfs，分别从两头都开始bfs，有交集就可以返回。
- 126题. Word Ladder II,时间复杂度要求很高，backtracking会超时，具体有几种解法:
 1. 一种可以先bfs，记录正向边，然后进行bfs.
 2. 第二种可以先bfs,记录父节点，也就是反向边，然后dfs从后往前查找。
- 669题. Trim a Binary Search Tree. 递归，首先验证root是否在范围内，否则把root更换为root.left/root.right. 然后分别对左右进行递归。
- 665题. Non-decreasing Array.对i的情况进行讨论.到底是nums[i]有问题还是nums[i+1]有问题.



## 9.4
- 564题. Find the Closest Palindrome. 把所有可能的结果存为candidates， 然后遍历选择最小的。如何选择candidates呢，用n的前一半，p，分别使用p，p+1，p-1，来组成*奇和偶*回文，同时考虑如果答案和n长度不同的情况，这时候需要把邻近的999999和1000001加入candidates.
- 381题. Insert Delete GetRandom O(1) - Duplicates allowed.跟380题很类似，这里使用`difaultdict(set)`而不是普通的`dict`.最关键的部分在`remove()`函数中，因为经过不断的交换之后，在存放index的容器中，顺序都乱了，所以不能用`pop()`而使用`discard`或者`remove`，在`list`中`remove`是`O(n)`的，而在`set`中`pop()`和`discard`可以看作是O(1).

## 9.3
- 218题. The Skyline Problem.时间复杂度`O(n^2)`.对每一个`building`的左上角和右下角遍历，用一个最大堆(Python中没有最大堆可以用-h代替h)维护高度，如果x(横坐标)的越过了`heap`里最顶(高)的,就`pop`，否则`push`，一旦高度跟`res`里最后一个不同，说明是一个`key point`.在Python中，`heapq`的`push`和`pop`都是`O(logn)`.java中也是(至少pop..)。
- 207题. Course Schedule.两种方法，第一种是拓扑排序，使用一个`queue`(`deque`)实现，第二种是`dfs`或者`bfs`.发现环路就返回`False`.
- 210题. Course Schedule II. 跟207一样，只需要记录拓扑排序。


## 8.31
- 56题. Merge Intervals. `Interval`是一个类的实例，然后只需要设置一个`start`和`end`来作为最大的起点和终点就可以更新`result`里。也可以用栈来实现。更为简单。也可以跟meeting rooms II一样的做法，排序两次，用两个指针来更新。
- 49题. Group Anagrams.用`tuple(sorted(x))`来作为`hash`的`key`,用`lib`来存储已经出现过的组合，并且`value`是`index`，然后可以在`result`里面存储。速度比一般的快。


## 8.19
- 62题. Unique Paths.DP问题，状态转移方程`P[i][j] = P[i - 1][j] + P[i][j - 1]`.
- 657题. Judge Route Circle.只需要count即可.
- 661题. Image Smoother.双循环即可。
- 662题. Maximum Width of Binary Tree.level order会tle,所以只能用递归。DFS,对左右节点记录在树中的`index`编号，用一个`dict`来维护，key是深度，`value`是`index`，空的就返回`None`, 这样便利一遍`map`就可以确定最宽的。

## 8.18
- 433题.Minimum Genetic Mutation.我的方法是用`backtracking`,用`diff`函数来判断差刚好1个字符，用`bfs`来查找。要在查找结束之后把`visited`和 `mutation`重置。其他方法使用栈或者队列。

## 8.16
- 15题. 3Sum.时间复杂度为`O(n^2)`.解法是，对于每一个数，把`target`设置为`0-nums[i]`,然后可以用2sum来解决，这里用的是双指针而不是字典，效果是一样的。要注意去重，包括`nums[i]`和`nums[l]`,`nums[r]`。

## 8.9
- 148题. Sort List. merge sort,一个merge函数用来合并，然后主函数拆分linkedlist，bottom-up。时间复杂度O(nlogn)，空间不算递归开销的话是O(1).

## 8.7
- 11题. Container With Most Water. 从左右开始，更新体积v，如果左右高度哪个低，就更新哪个，这样可以保证体积最大。有证明不过比较绕。
- 151题. Reverse Words in a String. split以后reverse，再拼起来即可。方法很多，可以全部倒过来以后对每个单词reverse，还可以用分治法，对空格左右分别递归。
- 388题. Longest Absolute File Path. 巧妙解法：用input.splitlines()直接获取每行的字符串，然后根据`depth = len(line) - len(name)`来确定深度，交替更新maxlen和pathlen[depth]。比较一般的做法是使用栈。

## 8.6
- 544题. Output Contest Matches.循环log(n,2)次，`res[i] = '(' + res[i] + ','+ res[n-1-i] + ')'`，或者用`zip()`.
- 2题. Add Two Numbers. 比较容易，新建一个linkedlist,把依次把l1和l2的val加进去就可以了，如果遇到进位就下一步加1.

## 8.5 
- 653题. Two Sum IV - Input is a BST.遍历一边树，节点存到一个hashmap，然后two sum.
- 654题. Maximum Binary Tree. 递归左右子树即可。

## 8.1
- 170题. Two Sum III - Data structure design. two sum 变形，Python的in dict时间复杂度几乎是O(1)，get()也是，解法还是哈希表.要注意重复元素，如果有两个重复元素就可以用.
- 479题. Largest Palindrome Product.很烦的题，要先构造回文数，再检查是否可以被n位的数整除.关键点是，如何优化时间复杂度，用Python总是会TLE。另外构造Palindrome的时候，为什么总是`2*n`长度？为什么不考虑奇数长度的Palindrome呢？我的一种猜测是当n足够大比如2以上的时候，因为Palindrome的范围会很大，所以很有可能在`2*n`长度的时候都会存在符合要求的数，这样不需要到`2*n-1`就可以返回结果了.


## 7.31
- 408题. Valid Word Abbreviation.只需要统计长度相等即可，注意一些边界条件，比如abbr以数字结尾，或者0开头,或者数字大于总长度.
- 69题. Sqrt(x).求平方根。可以用二分查找，也可以用牛顿法。也可以用bit manipulation.
- 125题. Valid Palindrome.双指针，如果不是alnum就+1.

## 7.29
- 157题. Read N Characters Given Read4.非常莫名其妙的一道题，主要注意的几个点，`buf`是接受字符的容器，而且大小分配好了，然后因为有可能文件长度比`n`还要小,所以要处理这种情况。做法就是用一个长度为4的`tmp`数组存`read4()`读进来的字符，然后传给`buf`.
- 532题. K-diff Pairs in an Array. 哈希表, O(n)解法。还要检查k是否小于0.
- 28题. Implement strStr(). 实现找到第二个字符串在第一个字符串中的起始位置。方法就是双循环，时间复杂度O(m*n)，使用kmp算法可以达到o(m+n)的时间复杂度.
- 652题. Find Duplicate Subtrees. backtracking，把


## 7.28
- 475题. Heaters. 比较麻烦的一道题, 解法是对每一个house选出来最近的一个heater, 记录距离，然后在所有的距离里选出来一个最大的. 如何对每一个house选最近的heater呢, 可以用下标的方式，也可以用二分法.
- 303题. Range Sum Query - Immutable. 因为会被调用很多次，所以见一个数组，`sum[j]`就是从1到j的和，直接`sum[j]-sum[i-1]`即可，稍微判断下`i=0`情况.

## 7.27
- 605题. Can Place Flowers.三连`0`就可以在中间插一个，但是还有两头这种情况，所以可以在一头一尾加上一个空的，再直接开始判断，或者也可以判断是否`i==0 和i==len(flowerbed)-1` 这两种情况。
- 581题. Shortest Unsorted Continuous Subarray.这道题有160个upvote，4个downvote，说明题目很好。O(nlgn)的解法最简单，就是排序，然后比较，index也有点tricky,O(n)的解法非常巧妙。[这里](https://discuss.leetcode.com/topic/89282/java-o-n-time-o-1-space)


## 7.26
- 633题. Sum of Square Numbers. 在`c`的开方内枚举`a`，然后`b = (c-a*a)**0.5`,如果b是整数那么返回true.
- 400题. Nth Digit.比较一般的做法，首先确定来自于那个数字段，再确定来自于哪个数，在确定是哪个数字。

## 7.25
- 58题. Length of Last Word. 可以用split(),或者从尾巴开始，先跳过‘ ’，到第一个不为空开始计数，知道到达最前面或者遇到‘ ’.
- 604题. Design Compressed String Iterator. 需要计数,计算当前字符个数，当为0的时候只想下一个字符，这道题只能用python3提交，不知道为什么。


## 7.23
- 645题. Set Mismatch.找出重复元素，然后找出丢失元素。最一般的就用哈希表，或者用一个长度为n的数组来存放出现的次数，等于2就是重复元素，等于0就是缺失元素.
- 643题. Maximum Average Subarray I. Sliding window. K是给定的，所以很简单。
- 644题. Maximum Average Subarray II.给定范围是大于等于K的，如果是完全不规定呢？还没有好的解决办法.答案用的是二分法。

## 7.17
- 526题. Beautiful Arrangement. Backtracking典型,检查是否合法，然后dfs，长度等于N就+1. 还可以top down solution, 非常快。还可以用cache存已经计算过的值，更快，贴一下代码 
 ```class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        def helper(i,X,cache = {}):
            if i == 1:
                return 1
            if X not in cache:
                cache[X] = sum(helper(i-1,X[:j]+X[j+1:])
                           for j,x in enumerate(X)
                           if x % i == 0 or i % x == 0)
            return cache[X]
        return helper(N, tuple(range(1,N+1)))
  ```

## 7.15 
- 67题. Add Binary.偷懒办法用内置函数，比较一般的做法就是按位相加，`carry`来存进位.

## 7.13
- 276题. Paint Fence. 挺麻烦的，因为要求最多不能超过两个重复颜色的，所以需要设定两个变量，一个保存下一步涂不同颜色`diff`，另一个保存相同颜色`same`，`diff, same = (diff+same) * (k-1), diff`.
- 507题. Perfect Number. 很容易暴力，然后优化，只需要迭代到平方根，`sum += i + num/i`.
- 624题. Maximum Distance in Arrays. 非常巧妙，先设定一个`MAX`，一个`MIN`，一个`res`，然后之后的每次遍历，都交叉比较，保证最大最小不在一个`list`里面.
- 225题. Implement Stack using Queues.跟232差不多，两种，一种使用两个`que`，另外一种方法是`push`的时候不断`pop`再`push`使得最开始`push`进来的push到最头上。

## 7.12
- 172题. Factorial Trailing Zeroes.计算有多少个`5`，`25`，`125`...累加即可，因为每个`5*2`都会产生一个`0`，`2`是足够用的，所以只需要计算`5`的个数.
- 374题. Guess Number Higher or Lower. 二分查找.
- 38题. Count and Say.非常无聊的题目，第`i+1`个字符串 就是上一个的`count and say`，计数生成字符串，或者用正则表达式。


## 7.11
- 637题. Average of Levels in Binary Tree. level order traversal可以直接解决。
- 538题. Convert BST to Greater Tree. 做倒序的`inorder`,先走到最后边，再往左递归，记录右边的和，不断累加。
- 232题. Implement Queue using Stacks.使用栈实现队列，两种方法，第一种push的时候直接push成队列的顺序，push时间复杂度O(n)，第二种是双栈，pop的时间复杂度O(1),最坏情况是O(n)。
- 441题. Arranging Coins.数学题，解方程，或者二分查找。
- 422题. Valid Word Square.验证沿对角线是否对称即可.

## 7.10
- 501题. Find Mode in Binary Search Tree. 简单办法是直接用前/中/后序遍历遍历一遍，然后用hashmap存次数，高级方法用`O(1)`space，就是用`pre`,`count`之类的来更新`mode`了。
- 434题. Number of Segments in a String. 直接`split()`然后`len()`.
- 637题. Average of Levels in Binary Tree.


## 7.7
- 263题. Ugly Number. 不断除2/3/5即可。
- 345题. Reverse Vowels of a String. 双指针。都符合条件就直接交换，否则各自+1.
- 367题. Valid Perfect Square. 二分法。

## 6.30
- 53题. Maximum Subarray. Dp问题，状态转移：`maxSubArray(A, i) = maxSubArray(A, i - 1) > 0 ? maxSubArray(A, i - 1) : 0 + A[i];`
- 270题. Closest Binary Search Tree Value.可以直接全部遍历一遍，这样没有利用到BST的性质。更好的做法是只便利一半，根据大小选择下一步是左还是右。

## 6.29
-  35题. Search Insert Position. 直接append然后排序可以解决，然而复杂度不好，Python的timesort复杂度最好能到O(n)，然而二分法只需要O(lg n),高下立判，Binary search.注意边界值.


## 6.28
- 628题. Maximum Product of Three Numbers. 先排序，最大值只可能是后三个，或者是前两个和最后一个的乘积。
- 326题. Power of Three. 作弊的方法是找出最大的int 1162261467，然后看1162261467%n==0，比较一般的就是不断除3.
- 594题. Longest Harmonious Subsequence.存一个`hashmap`，如果里面也有`num+1`，那么更新最大长度。

## 6.25
- 415题. Add Strings.要求加两个字符串类型的数，但是不准转换为`int`,做法就是一个一个读字符串，然后设置carry位存进位，然后累加起来。

## 6.14
- 541题. Reverse String II. Java C++可以swap,双循环。Python可以利用切片。也可以转换成`list`再处理，这样最后剩下的小字符串就不需要单独考虑了，因为`list`可以处理边界溢出的情况。比如`s = [1,2,3,4], s[2:10] =[3,4]`
- 551题. Student Attendance Record I.正则表达式或者直接计数.Python 可以用`s.count('A')`
- 543题. Diameter of Binary Tree.分别对左右各自取最大深度，再加起来.
- 572题. Subtree of Another Tree.这题是Same Tree的变种，直接拿了same tree的答案来用了。先检查是否是same tree，如果不是，然后需要分别检查左右节点是否是isSubtree。

## 6.12
- 563题. Binary Tree Tilt.要计算所有左右子树的差，不光光是节点对，所以要用递归，如果要先看左右值，就用后序遍历，然后返回`left+right+root.val`.
- 455题. Assign Cookies. 双指针.
- 506题. Relative Ranks.数组操作，用`hashmap`来存排名，前三替换.
- 617题. Merge Two Binary Trees.递归.
- 256题. Paint House.DP,对三种颜色都取最小，然后再`min()`.注意+=，可以在原数组上操作，很关键。

## 6.9
- 599题. Minimum Index Sum of Two Lists.用哈希表，key是字符串，value是index,利用哈希表查询是O(1)的特点，循环更新最小值，记录结果.
- 492题. Construct the Rectangle.开方之后查找能整除的。
- 598题. Range Addition II. 分别求两个坐标的最小值相乘.
- 530题. Minimum Absolute Difference in BST. inorder遍历,可以保存BST的序列。然后比较更新minimum.*大坑*这里本想用Python写个跟java一样的版本，才发现python的不可变类型在递归中是不会变的，所以用一个minimum来传递是不可实现的。*对于不可变对象作为函数参数，相当于C系语言的值传递；对于可变对象作为函数参数，相当于C系语言的引用传递*。

## 6.7
- 477题. Total Hamming Distance.这题跟260题类似，思路就是对于每一个位上，有`p`个`1`和`n-p`个`0`，会产生`p*(n-p)`个distance，对于32位每个位跑一边加起来就可以了。
- 191题. Number of 1 Bits. 无符号类型，java需要用`>>>`,`n&=(n-1)`或者`n = n&(n-1)`可以每次把最右边置0，知道全部是0.或者就每次`n&1`,然后>>>1。还可以`return Integer.bitCount(n);`
- 137题. Single Number II. 巧妙的办法，<https://discuss.leetcode.com/topic/2031/challenge-me-thx>.
- 231题. Power of Two. `n&(n-1)`可以移除最右边(最低位)的`1`，如果是power of 2就只有1位是`1`，所以可以用`return (n>0 && !(n&(n-1)))`，Jave里`!`不能用在`int`类型上。
- 342题. Power of Four.`return num > 0 && (num&(num-1)) == 0 && (num & 0x55555555) != 0;`.`0x5555555`是所有奇数位上是1的数.用它来保证是4的power，还可以用`(num-1)%3 == 0`来保证。
- 405题. Convert a Number to Hexadecimal.每处理一位后右移4位。负数的话要 `num+=2*32`.或者`num = (-num ^ 0xffffffff) + 1`.
- 190题. Reverse Bits. 镜像移动两个数，用`m+=n&1`来赋值，先右移再赋值，然后再右移。
- 401题. Binary Watch. 每个灯代表二进制的一个位.用一个双层循环来遍历一下所有的可能，如果灯的数量(`1`的个数)等于 num,那么就是一个解。

## 6.6
- 371题. Sum of Two Integers. 有点小复杂,具体<https://www.hrwhisper.me/leetcode-sum-two-integers/>.
- 260题. Single Number III. 很复杂，首先xor得到两个的`xor`,然后用 `xor &= -xor`得到最右边的`1`，也就是说这两个数，在这个位置上是不同的(`^`的性质)，然后根据这个，可以把这些数根据`num&xor == 0`分成两组，对每组进行`xor`以后，就得到了两个数.


## 6.5
- 243题. Shortest Word Distance. 双指针。
- 244题. Shortest Word Distance II. 用`hashtable`把`index`都存起来。然后取出最短距离。注意时间复杂度，双循环是O(m*n),单层循环是O(m+n)。
- 245题. Shortest Word Distance III. 这题允许重复元素. 所以当遇到重复元素的时候，就把上一个遇到这个元素的位置记录下来，更新后面的.

## 6.4
- 521题. Longest Uncommon Subsequence I. 这题就是用来搞笑的。相等就返回`-1`，不想等就返回max(len(a),len(b)).
- 522题. Longest Uncommon Subsequence II. 先降序排序，再对每一个比较。其中用到了迭代器.
- 606题. Construct String from Binary Tree. 前序遍历，用递归即可。需要注意的是在Python里`str`是不可变类型，不能用来作为递归时候的变量传递.很关键.
- 448题. Find All Numbers Disappeared in an Array.解法非常巧妙，inplace 的第一遍时候把所有出现过的数值设为负，剩下的正的index就是没出现的数值了。不用inplace的话直接`return list(set(range(1, len(nums)+1)) - set(nums))`.

## 5.19
- 557题. Reverse Words in a String III. 用`x[::-1]`一行。

## 5.18
- 561题. Array Partition I. 排序切片求和。
- 566题. Reshape the Matrix. `res[i/c][i%c] = nums[i/m][i%m]`
- 575题. Distribute Candies. Python可以用`set`一行解决。

## 5.17
- 216题, Combination Sum III. 这题还是backtracking， 一样的模版。只需要每次都全部循环即可。
- 377题, Combination Sum IV. 这题可以用backtracking，但是会MLE，因为path这个需要大量的内存，所以只能用DP做，状态转移方程`comb[target] = sum(comb[target - nums[i]]), where 0 <= i < nums.length, and target >= nums[i].` Base case `comb[0] = 1`这里有点不明白。在中间过程中，说明`target = nums[i]`,说明只有这一种情况，所以设置为1。
- 78题,Subsets. 一样的模版。另外一种解法是`bit manipulation`。不会。
- 90题. Subsets II. 跟`Combination Sum II.`一样，去重即可.
- 46题, Permutations, 一样的模版。
- 47题, Permutations II, 不同之处在于去重，用一个used的数组存一下。不用backtracking的话还有别的解法。不懂！！
- 131题. Palindrome Partitioning. 同一个模版，需要写个函数判断是否是Palindrome。
- 246题. Strobogrammatic Number. 哈希表存一下对称的，然后比较一下即可。
- 247题. Strobogrammatic Number II. 考虑奇偶情况，结合递归，排列组合.
- 447题. Number of Boomerangs. 用哈希表存距离,求和。

## 5.16
- 39题. Combination Sum. backtracking问题，排序可以提升性能。在循环内部判断剪枝。剪枝就像是get rid of a subtree.
- 40题. Combination Sum II. 跟39跟相似，两个区别是递归的时候从`i+1`开始，和验证是否是重复元素，这个很关键，去重是横向的不是纵向的，而且是，大于，而不是大于等于，所以`1,1,6`这种可以过，两个`1`不会重复。剪枝很关键，非常提高性能.

## 5.13
- 278题. First Bad Version. 二分法，注意边界值.`(left + right) / 2`和`left + (right - left) / 2`区别在于`left + right` may cause the Integer Overflow, meaning that `left+right` > 2147483647.


## 5.11
- 293题. Flip Game. `if`判断就可以，用切片，一行可以搞定。 
- 520题. Detect Capital.py. 直接用三个内置函数就可以了.弱智题.
- 504题. Base 7. 简单题,注意正负，直接整除加上取余。

## 3.8
- 413题. Arithmetic Slices. DP问题。
- 535题. Encode and Decode TinyURL. 设计模式问题，主要就是使用`random`和`string`生成6位的随机字符串，用两个`hashmap`来存长短对应关系。用`hashmap`可以很好的解决重用问题.

## 2.26
- 406题. Queue Reconstruction by Height. 先排最高的，然后排第二高的，一个个插入，`index`就是自带的`index`. 用`lambda`表达式可以简化排序.

## 2.25
- 280题. Wiggle Sort.这题看起来复杂，其实只需要维护一个`小大小大小大`的顺序就行了，只需要对奇偶两种情况讨论，交换`nums[i-1]`和`nums[i]`即可。这里不需要对`i=0`进行特殊讨论是因为在`i=1`的时候把`0`概括进去了。
- 324题. Wiggle Sort II . 这题很难，因为必须大小交错，出现相等的情况交换前后元素的方法就不管用了。Python的做法比较简单，固定排序顺序，倒序之后交错插入。另外一种解法，用中位数， `(1 + 2*index) % (n | 1)`可以把`index[0,1,2,3,4,5]`映射为`[1,3,5,0,2,4]`.  然后把`mapped`的`index`交错排回去.
- 513题. Find Bottom Left Tree Value. 可以用队列也可以用递归。队列可以用`level-order traversal`，从右往左，最后一个node就是我们要找的。或者用递归，记录树高，出现更高的就更新`res = node.val`.

## 2.24
- 366题. Find Leaves of Binary Tree. 分别对左右子树递归，从下到上遍历每个节点，典型的`bottom-up`解法，记录每个节点的高度h,根据`h` remove leave. 时间和空间都是O(n).
- 346题. Moving Average from Data Stream. 有一种简便做法是用collections里的deque，设定`maxlen = size`.另外用`slice`会导致速度慢，可以直接用长度为`size`的中间变量`list`，存储,然后更新。
- 266题. Palindrome Permutation. 用`set`数据结构即可。还可以用`Counter`,还可以用`bitset`.

## 2.23
- 338题. Counting Bits. 倒过来想，一个数 `*2` 就是把它的二进制全部左移一位，也就是说`1`的个数是相等的. 那么我们可以利用这个结论来做,`res[i /2]`然后看看最低位是否为`1`即可`(i & 1)`,(上面`*2`一定是偶数，这边比如15和14除以2都是7，但是15时通过7左移一位并且`+1`得到，14则是直接左移),所以res[i] = res[i >>1] + (i&1)
- 359题. Logger Rate Limiter. 题目看上去很复杂，其实很简单。用一个`hashmap`就可以解决。可能的follow up可能有，比如消息很多，不需要存储很少出现的消息以节省空间，这时候可以用一个队列存消息，另一个`hashmap`存时间，实现小空间。

## 2.21
- 419题. Battleships in a Board. 这题有个窍门，就是既然战船是一条状的，可以只数船头，那么船头只要符合`board[i][j] == 'X' and (i == 0 or board[i-1][j] == '.') and (j == 0 or board[i][j-1] == '.')`就可以。其他方法还有经典的flood fill algorithm,用dfs或者bfs.

## 2.20
- 496题. Next Greater Element I. 这道题非常适合面试。
  + 首先很容易想到一个`O(m*n)`的解法，对`nums`建立一个hashmap,存每个元素的`index`,然后遍历`findNums`，找对应的`index`，再往后找`greater number`，这个虽然简单，但是有个边界值非常需要注意，第一种是j遍历到最后，还是没找到，这时候`append(-1)`,还有一种就是到最后了，找到了，这时候不加`-1`，还需要注意循环体的边界，如果`dic[n]+1 == len(nums)`循环体是不执行的。
  + 第二种是时间复杂度`O(m+n)`,直接对`nums`建一个hashmap，`key`是每一个`number`，`value`直接是`greater element`,怎么实现呢，需要用一个栈，维护一个递减的序列，For example `[9, 8, 7, 3, 2, 1, 6]`, the stack will first contain `[9, 8, 7, 3, 2, 1]` and then we see `6` which is greater than `1`, so we pop `1 2 3` whose next greater element should be `6`. 最后直接查询`findNums`的每一个元素，返回对用的`next greater element`或者 `-1`.
- 503题. Next Greater Element II. 是496的follow up. 一样的思路，除了最基本的`O(n^2)`方法之外，还有两种方法都是用栈,循环体中的边界用`2*n`,然后`i%n`来把头尾接起来。一种使用`(index, number)`作为`key`，存储 greater number,注意进栈的时候，只对`i<len(nums)`的元素进栈。第二种做法是只存`index`,初始化一个`[-1*n]`的数组，其他的一样。

## 2.15
- 75题. Sort Colors. in place, 设置三个指针`start, end, i`, 然后`i < end`和`i > start`的时候`swap`就可以。还有种解法比较难理解，就是 We keep a loop invariant that [0,i) [i, j) [j, k) are 0s, 1s and 2s sorted in place for [0,k).

## 2.14
- 285题. Inorder Successor in BST. 这题的解法是比较`root.val`和`p.val`的大小，考虑两种情况：
  + 第一种，`root.val > p.val`这种情况下 `root`是可能作为`p`的successor的，所以把res的值更新为root，然后往左边查找。
  + 第二种，`root.val <= p.val`, 这种情况下，`root`事不可能作为`p`的seccesor的，左子树也不可能，只有往右边找，`root = root.right`.
最后迭代到`root = None`,这时候返回`res`就可以了。这题递归的方法也可以做，比较难以理解。

## 2.13
- 223题. Rectangle Areaz. 这题非常简单，只需要判断overlap是否存在。
- 461题. Hamming Distance. Bit manipulation, 这题用内置的Python/java 中的 `bin()` 或者 `Integer.bitCount()`即可. 效率做法是 `xor = xor &(xor - 1)`,可以迭代最少的次数。
- 476题. Number Complement. Bit manipulation, 这题先造出一个`1111111`的数，然后与`num`异或即可，如何造出这个`111111`呢？java可以 `(Integer.highestOneBit(num) << 1) - 1`, python可以用1一直`<<`然后-1.
- 500题. Keyboard Row, 这题用的自己的写法，效率挺高的，主要就是建立一个`hashmap`来存储每个字母所在的行数，然后对每个word对每个letter查询，如果和每个word的第一个不一样，就下一个word.`res.toArray(new String[0])`来把`ArrayList`转换为`String`.
- 339题. Nested List Weight Sum. 可以用迭代或者递归，保存`depth`,比较简单。


## 2.12
- 17题. Letter Combinations of a Phone Number，这题有点难，本来想用Python的`zip`但是写不出来，看了答案比较一般的做法是用回溯，back-tracking,比如[这里](https://discuss.leetcode.com/topic/37976/fast-backtracking-easy-to-understand-with-explanations). 巧妙解法有用迭代一次次出队列再入队列。查看`peek()`的长度实现过一遍所有元素的方法。
- 516题. Longest Palindromic Subsequence. 跟5非常的相似，区别在于必须要满足序列这个要求。方法也是dp，状态转移方程，  
`dp[i][j]`: the longest palindromic subsequence's length of substring(i, j)  
State transition:  
`dp[i][j] = dp[i+1][j-1] + 2 if s.charAt(i) == s.charAt(j)`  
otherwise, `dp[i][j] = Math.max(dp[i+1][j], dp[i][j-1])`  
Initialization: `dp[i][i]` = 1  
Python会TLE.

## 2.11
- 5题. Longest Palindromic Substring. 这题两种做法,
  + 一种是按部就班的dp，状态转移方程是`P(i,j)=P(i+1,j-1) and S(i)=S(j)`,初始条件，`P(i,i) = True`和`P(i,i+1) = True`.用二维数组来存`True`or`False`,从长度为2的字符串往后面枚举，更新最大长度。时间复杂度O(n^2),空间O(n^2).
  + 另一种是选n-1个中间节点，从中间往两边拓展，分别对奇数和偶数两种讨论，更新`low`位置和最大长度`maxLen`，下标很容易搞错，amazon的重点题。时间复杂度O(n^2),空间复杂度O(1).
  + 还有一种更厉害的解法叫Manacher算法，时间复杂度O(n), 空间复杂度O(n)。不做讨论了。比较复杂。

## 2.8
- 380题. Insert Delete GetRandom O(1). In interview setting, it's perfectly reasonable to assume hash table add/delete operations are O(1). 这题需要实现O(1)的时间复杂度， 插入的需要用一个dict来存index，在删除的时候把最后一个元素跟删除的交换，pop掉最后一个，更新dict里的index。或者也可以用python自带的set数据结构来实现，但是就有种骑马找马的感觉了。java的写法中，ArrayList的`contains`方法时间复杂度是O(n)，所以这里要查询`Hashmap`来判断是否存在`val`. 这里对性能很关键。[这里](http://infotechgems.blogspot.com/2011/11/java-collections-performance-time.html)是java中数据结构的时间复杂度。
- 138题. Copy List with Random Pointer.![](http://images.cnitblog.com/i/627993/201405/221027256064414.jpg)
  + 首先，在原链表的每个节点后面都插入一个新节点，新节点的内容和前面的节点一样。比如上图，1后面插入1，2后面插入2，依次类推。
  + 其次，原链表中的random指针如何映射呢？比如上图中，1节点的random指针指向3，4节点的random指针指向2。如果有一个tmp指针指向1（蓝色），则一条语句：tmp.next.random = tmp.random.next；就可以解决这个问题。
  + 第三步，将新的链表从上图这样的链表中拆分出来。
另外用字典也可以做。字典会导致space complexity编程O(n). time complexity都是O(n).


## 2.7
- 387题. First Unique Character in a String, Python的解法很简单，过一遍字母表就可以，存储`index`，输出最小的`index`时间复杂度是O(n)。比较好的解是用hash表对每个字符统计出现次数，然后再根据字符串顺序输出次数为1的字符，但是字符串太长，我们要找的字母在字符串最后，就会浪费很多效率，所以最优解是在hash存字符出现次数的时候同时存`index`，就可以实现只扫一遍。c++可以用`std::pair`实现。
- 459题. Repeated Substring Pattern. Python的做法是把两个`str`连接起来，去头去尾，然后在这个长的链接`str`里面寻找本来的字符串`str`,`find()`方法还能返回`index`. 直接判断可以用`in`，可以做到一行。  
`return str in (str+str)[1:-1]`  
比较一般的做法是KMP算法,时间复杂度应该是O(n)。参见<http://www.ruanyifeng.com/blog/2013/05/Knuth–Morris–Pratt_algorithm.html>. 还可以用试除数的方法，复杂度worst case是O(n^2).
- 155题. Min Stack，正常写法，因为要求`getMin()`O(1)的查询速度，所以要牺牲空间来维护最小值，[这里](http://stackoverflow.com/questions/685060/design-a-stack-such-that-getminimum-should-be-o1)说的很清楚，如果`getMin()`是O(1)，那么当`pop()`出去的如果是最小值，那么`pop()`会变成O(n),而且再`push()`的时候也是O(n),如果用tuple(或者另一个ministack)来存储值的话会增加空间。所以基本上都是trade-off. java的写法要使用一个栈的话必须`push`两次，一次记录当前的`min`,一次记录`x`，还可以优化为只有更新`min`的时候才把`min`进栈。


## 2.6
- 337题， House Robber III, 还是dp，但这次是树，递归的时候巧妙的使用了一个tuple，来记录前面的最优解。挺难的。要想一会才能明白。[这个解法](https://discuss.leetcode.com/topic/39846/easy-to-understand-java/3)很不错。
- 236题，Lowest Common Ancestor of a Binary Tree,可以用递归来解决，递归寻找两个带查询LCA的节点`p`和`q`，当找到后，返回给它们的父亲。如果某个节点的左右子树分别包括这两个节点，那么这个节点必然是所求的解，返回该节点。否则，返回左或者右子树（哪个包含`p`或者`q`的就返回哪个）。java解法的一个小trick:  
`return left==null? right : right == null? left: root;`
- 20题，Valid Parentheses，用栈，对于前括号一律把对应的后括号进栈，这样实际上字符串里对应的后括号和栈里的是一致的，不一样就返回`False`。java中`stack`是`vector`的延伸，性能上不好，用`deque`来代替`stack`比较好.
- 48题，Rotate Image，先上下交换再沿对角线交换。注意边界值避免重复交换，Python的解法比较多，妙用`zip(*)`可以实现对角线交换。`matrix[:]`可以直接inpalce修改。

## 2.5
- 213题，House Robber II, 同样是dp，需要转换成House Robber I来做，因为第一个和最后一个不能同时抢，所以分成两个子问题，一个是`nums[0]~nums[n-2]`,另一个是`nums[1]~nums[n-1]`，然后`max`一下，需要特别注意的就是边界值。

## 1.22
- 70题，dp问题，本质是Fibonacci,可以暴力，时间复杂度`2^n`,空间`O(n)`,递归树的深度可以到`n`.也可以动态规划，存一个数组然后更新，`O(n)`space，或者连数组都不用直接三个变量存。最优解是直接用Fibonacci公式，`pow()`方法用`log(n)`时间。
- 198题，House Robber I, 同样是dp问题，需要状态转移方程：`dp[i] = max(dp[i - 1], dp[i - 2] + num[i])`.

## 1.17
- 485,487题，weekly contest,比较简单，487可以用一步就可以实现，用两个变量存low位置。

## 1.11
- 417题，Pacific Atlantic Water Flow,这题用DFS, 反向从边上往中间迭代，能到达的标记为True,分别维护两个矩阵一个P一个A,最后如果两个矩阵同一个位置都是True那么这个点是。
- 329题，Longest Increasing Path in a Matrix. 这题跟417题很像，对每一个点进行dfs，维护一个cache来记录长度，需要注意的是在dfs这个函数里面的计数，要保证记录最长长度，就要用`max()`函数来维护。这道hard题总的来说还是不难的。
- 101题， Symmetric Tree, 这题用递归，分别验证`root`左右值，然后递归左右节点。或者用`level order traversal`也可以，用`list`和反转之后的`list`比较，或者用`stack`，一次`append`一个`tuple`,验证是否相等或者是否都为空。

## 1.7
- 109题，两种方法
  + 第一种是快慢指针，时间复杂度O(nlgn)。用慢指针找到`inorder`的中点，分别对两边进行递归。中间要切断一些边。
  + 第二种是Bottom-up方法，用index来表示中点，一层层递归下去，先选最左边的结点，然后接到root上，然后接上右边的，整个过程是从下往上合并。因为先计算长度size，O(n)时间，然后`inorder reconstruction`,时间O(n)，所以总体时间是O(n). Space 是constant space所以是O(1) space.
- 还有一个大坑是，一不小心就空格和tab混合使用了，这样加注释的时候会产生不一样的注释缩进，导致无法AC！fuck！耽误一小时时间。
- 200题，number of islands，用DFS，把每一个遇到的‘1’(岛)，寻找它相连的其他岛，变为`0`，因为我们把相连的`1`看作一个。时间复杂度O(mn),空间复杂度O(mn),mn为尺寸。
- 394题，Decode String,又有两种做法。这题很有意思，也不太容易。
  1. 第一种双栈，一个记录数字，也就是k，一个记录字符串，每次遇到'['的时候更新数字栈，同时也要压一个空的`''`进字符串栈，然后用`-1`索引来操作栈，最后字符串栈的第一个元素就是完整的字符串。这是比较一般的做法。
  2. 第二种是用`python`的特性，用`stack = [['',]]`这样形式的栈，更新数字的时候，用`stack.append(['', int(num)])`,这样有数字的情况下就会自动嵌套，最后同样输出第一层的第一个元素。

## 1.6
- 450题，删除BST的结点。
  + 一种做法是用左孩子的最右边(最大)结点，把右孩子接上去，会增加树的高度，影响查询速度。还可以把左孩子接到右孩子的最左端。一样的。
  + 另外一种做法是吧root替换为右孩子最左边(小)的节点，然后对右孩子递归操作。缺点是有的时候改那么多`val`不如改reference
- 108题，把有序array编程平衡BST，用递归很简单就寻找中位数，找到root，再对左右结点递归操作。
- 114题，Flattern Binary Tree,把BST压平。
  + 第一种做法是用递归，先把左右子树递归压平。再把右子树连接到左子树后面,再把左子树连接到`root.right`,最后把`root.left = None`. 
  + 第二种做法，叫 Morris traversal，非常有趣，做法是把左子树连接到`root.right`，然后找到左子树中最右边的结点，把右子树连接上去，然后再把左子树连接到`root.right`,然后`root = root.right` 一个个循环下去。空间复杂度O(1),时间复杂度O(n).厉害了
- 105和106题，Constuct Binary Tree from Preorder and Inorder/Inorder and Postorder Traversal。这两题[水中的鱼](http://fisherlei.blogspot.com)的文章<http://fisherlei.blogspot.com/2013/01/leetcode-construct-binary-tree-from.html> 有详细的解释。主要原理就是利用前序/后序遍历找到`root`，然后根据`root`分割`inoder`,然后递归左右子树。唯一一点要说的是`Python`写的中间切片操作会生成新的数组，导致MLE或者一些奇怪的bug,所以最好用`self._build_tree(inorder, low_in, high_in, postorder, low_post, high_post)`




## 1.5
- 107题，104的变形，倒过来就行了，也可以用栈加level标记高度的方法，速度还是比简单方法慢。
- 110题，Balanced Binary Tree, 用递归写比较容易，求左右树高，绝对值小于1，同时验证左右子树是否是balanced，时间复杂度O(n)。
- 111题，求最短叶子的高度，用递归，对每一层min，如果有左右节点有一个不存在的情况下就max。或者用`level order traversal`,遇到左右两个字节点都是`None`的情况下就可以直接返回树高。

## 1.4
- 104题，把树按照高度一层一层输出，ez题，一层层循环更新当层结点就行了。

## 12.1
- 230题，寻找二叉搜索树中第k个值，直接用inorder遍历然后存储成数组，然后取出结果。discuss看到有人说的生成器的用法，用`yield`语法

# 11.24
- 94题和144题，分别是树的前序遍历和中序遍历，递归很简单。主要用迭代的方法做，用栈，前序遍历简单直接右-左顺序压栈就可以。中序遍历难一点，要先压栈到最左边，然后不断往`node.right`走，如果没有right那么就会pop中间节点，就是我们想要的流程。 
- 145题，后序遍历，两种解决方法：
    1. 第一种双栈，第一个栈做左右交换的前序遍历，也就是说先压`node.left`，再压`node.right`，这样用第二个栈把节点都pop出来就是后序遍历。时间复杂度`O(n)`.
    2. 第二种解法是用pre记录上一个节点，我们使用`prev`变量跟踪上一次访问的节点。假设栈顶元素是`curr`,当`prev`是`curr`的父节点时，我们正在向下遍历树。此时，优先遍历`curr`的左孩子（将左孩子压入栈）。如果没有左孩子，再看右孩子。如果左右孩子都不存在（`curr`是叶节点），就输出`curr`的值并弹出栈顶元素。如果`prev`是`curr`的左孩子，我们正在从左子树向上遍历。我们看一下`curr`的右孩子。如果可以，就从右孩子向下遍历（将右孩子压入栈），否则打印`curr`的值并弹出栈顶元素。如果`prev`是`curr`的右孩子，我们正在从右子树向上遍历。打印`curr`的值并弹出栈顶元素。时间复杂度O(h), h为树高

## 11.22
- 235题，注意是二叉搜索树，BST，所以可以用value直接算，写了个栈竟然不对。

## 11.20
- 463题，双循环，每一个方块也就是1，加4，每遇到一个邻居-1
- 462题，排序，然后一个循环。时间复杂度O(nlogn),有时间复杂度O(n)的算法，就是求中位数的复杂度。
- 226题，反转二叉树，著名的Max Howell梗。直接交换就行了，然后递归。或者用DFS

## 11.17
- 404题，简单的递归或者DFS

## 11.8
- 113题，可以用DFS，判断是否和为sum，然后就加入res，或者用递归，在不同的层，如果不符合就return了None，这个应该是深层复制, 递归的时候是由下向上的，一层层的下去，再一层层地返回
- 437题，可以用递归写出O(n)时间复杂度的算法，用哈希表维护一个从root到当前node的路径之和，和有这样路径和的路径个数，然后如果从root到当前node的路径和`so_far - s`存在hashtable里面，那么说明找到了子路径，`res=dic.get(so_far,0)+1`。然后递归。注意在完成一个节点的时候，就在hashtable里面，把root到当前node的路径和个数-1

## 11.7
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

## 11.6
- 447，104，100这三题都是树，都是树的遍历，可以用递归，DFS或者BFS写。
- 112题，递归
- 257题，用递归可以写，也可以用DFS or BFS 写，path保存路径，要对每一个节点单独用一个path记录路径，所以用list或者tuple来匹配节点和他的单独路径。

## 11.5
- 287题，用法，时间复杂度O(nlgn)，另外有O(n)复杂度的算法，用快慢指针寻找环,要推导一些边界值，代码不是很复杂。
- 168和171题，同一个问题，168注意字母的临界值，用ascii码匹配
- 4题，回忆求一个array的中位数用divide and conquer 可以在linear time 解决，具体就是分三段，小于，等于，大于，然后递归(算法概论）。这题是求两个sorted的array的中位数，可以利用sorted的这个性质来减小时间复杂度，达到O(log(m+n))。具体是:把`nums1`和`nums2`都割成两半，比较A和B前一半最后一个值大小，较小的那个不可能包含我们要找的k值，所以缩减了A的一半大小，然后递归。原理就是这样，要注意很多边界值。

## 11.4
- 229题，还是Moore voting algorithm，用两个容器存candidate，迭代的时候注意不能让同样的值被两个容器同时出现，同样的candidate要在一个容器
- 167题，two sum II,用哈希表没什么好说的，或者头尾指针往中间找(题目说拍好序的)，或者还可以用二分查找。时间复杂度O(nlgn)

## 11.2
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

## 11.1
- 118和119题，杨辉三角，需要判断好边界值，119用O(k) space,在一行上面迭代

## 10.31

- 169题，摩尔投票 Moore voting algorithm,原理进出栈,只需要O(1)空间  
比哈希表省空间
- 121题，动态规划， kadane algorithm 时间复杂度O(n)

## 10.30
- 189题，inplace修改数组，如果`nums = ...`就是创建新数组，如果`nums[:]`就是在原来数组修改

## 10.29
- 414题，heapq 可以用来做topk，O(n)时间
- heapq 并不是以大小排序的。heap[0]代表最小,  
heapq.heappushpop() 先push再pop一气呵成 速度快

- `cmp`在3.0中被移除了，比如这个比较大小的 
	```
	nums.sort(cmp= lambda a, b: -1 if b == 0 else 0)
	```

- 排序时间复杂度 `O(lgn)`， python内置的`sorted`是timesort ，很高级，虽然复杂度是 `O(lgn)`

## 10.28
- 438题，用sliding window,用固定长度的字典，然后往后移动

## 之前的记不清哪天了
- 204题，找质数，512曾经的考试题 = =，很蠢的做法是对每一个数，判断是否是质数，用循环循环到n^1/2, 更巧妙的办法就是从开头开始把235...的倍数都标记成非质数，时间复杂度大大降低