# LEETCODE PROBLEM 98 : VALIDATE BINARY SEARCH TREE
# https://leetcode.com/problems/validate-binary-search-tree/description/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root.left == None and root.right == None:
            return True
        if root.left == None:
            if root.val < root.right.val:
                return self.isValidBST(root.right)
            return False
        if root.right == None:
            if root.val > root.left.val:
                return self.isValidBST(root.left)
            return False
        if root.val <= root.left.val or root.val >= root.right.val:
            return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)

left = TreeNode(val=2)
right = TreeNode(val=2)
middle = TreeNode(val=2, right=right)
solution = Solution()
print(solution.isValidBST(middle))