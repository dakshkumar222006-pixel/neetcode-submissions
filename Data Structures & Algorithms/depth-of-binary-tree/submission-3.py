# Definition for a binary tree root.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        maxleft,maxright=0,0

        if root.left is not None:
            maxleft = self.maxDepth(root.left)
        if root.right is not None:
            maxright = self.maxDepth(root.right)

        return 1+max(maxleft,maxright)
        