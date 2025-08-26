# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(node, sum_val):
            if not node:
                return False
            if not node.left and not node.right:
                return True if sum_val + node.val == targetSum else False
            return helper(node.left, sum_val + node.val) or helper(node.right, sum_val + node.val)
        return helper(root, 0)