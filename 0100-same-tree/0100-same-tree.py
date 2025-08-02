# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def checkSame(parent1, parent2):
            if not parent1 and not parent2:
                return True
            elif not parent1 or not parent2:
                return False
            if not parent1.right and not parent2.right and not parent2.left and not parent2.left:
                return parent1.val == parent2.val
            if parent1.val == parent2.val:
                return checkSame(parent1.left, parent2.left) and checkSame(parent1.right, parent2.right)
            else:
                return False
        
        return checkSame(p, q)