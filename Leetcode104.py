# LEETCODE PROBLEM 104 : MAXIMUM DEPTH OF BINARY TREE
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root == None:
            return 0
        if root.right == None and root.left == None:
            return 1
        if root.right == None:
            return 1 + self.maxDepth(root.left)
        if root.left == None:
            return 1 + self.maxDepth(root.right)
        return max(1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right))

s = Solution()
n15 = TreeNode()
n7 = TreeNode()
n20 = TreeNode(left=n15, right=n7)
n9 = TreeNode()
root = TreeNode(left=n9, right=n20)
print(s.maxDepth(root))