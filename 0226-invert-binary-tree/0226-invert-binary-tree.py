# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(root):
            if (root==None):
                return None
            rightsubtree = invert(root.right)
            leftsubtree = invert(root.left)
            root.right = leftsubtree
            root.left = rightsubtree

            return root
        return invert(root)
        