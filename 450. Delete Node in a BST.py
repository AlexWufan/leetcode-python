# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root: return None
        if root.val == key:
        	if root.left:
        		most_right_in_leftchild = root.left
        		while most_right_in_leftchild.right:
        			most_right_in_leftchild = most_right_in_leftchild.right
        		most_right_in_leftchild.right = root.right
        		return root.left
        	
        	else:
        		return root.right
        		
        		
        elif root.val > key:
        	root.left = self.deleteNode(root.left, key)
        else:
        	root.right = self.deleteNode(root.right, key)
        return root

#上面这种做法是用左孩子的最右边(最大)结点，把右孩子接上去，会增加树的高度，影响查询速度。还可以把左孩子接到右孩子的最左端。一样的。
#另外一种做法是吧root替换为右孩子最左边(小)的节点，然后对右孩子递归操作。缺点是有的时候改那么多值不如改reference



        #下面的做法有问题，首先是看错了不是输出level order traversal，只需要输出root。这是一个level order traversal的解法，傻逼

        
        if not root: return []
        res, level = [], [root]
        while level:
            tmp = []
            for node in level:
                if node:
                    res.append(node.val)
            print res
            for node in level:
                if node:
                    if node.left and node.left.val!=key:
                        tmp.append(node.left)
                    elif node.left and node.left.val == key:
                        if node.left.right:
                            tmp.append(node.left.right)
                            node.left = node.left.right
                            node.left.right.left = node.left.left
                        elif node.left.left:
                            tmp.append(node.left.left)
                            node.left = node.left.left
                        else: pass
                    
                    if node.right and node.right.val!=key:
                        tmp.append(node.right)
                    elif node.right and node.right.val == key:
                        if node.right.right:
                            tmp.append(node.right.right)
                            node.right = node.right.right
                        elif node.right.left:
                            tmp.append(node.right.left)
                            node.right = node.right.left
                        else: pass

            level = tmp
        return root

