# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def helper(root):
            if not root.left and not root.right:
                return 1
            elif not root.left:
                return helper(root.right) + 1
            elif not root.right:
                return helper(root.left) + 1
            else:
                return min(helper(root.left), helper(root.right)) + 1
        return helper(root)