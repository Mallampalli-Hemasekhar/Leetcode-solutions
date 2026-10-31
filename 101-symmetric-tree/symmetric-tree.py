# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        return self.search(root.left,root.right)
    def search(self,r1,r2):
        if r1 is None and r2 is None:
            return True
        if r1 is None or r2 is None:
            return False
        if r1.val != r2.val:
            return False
        return self.search(r1.left,r2.right) and self.search(r1.right, r2.left)