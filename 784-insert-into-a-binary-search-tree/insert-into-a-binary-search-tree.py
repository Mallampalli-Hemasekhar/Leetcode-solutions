# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if root is None:
            nn=TreeNode(val)
            root=nn
            return root
        if root.val<val:
            root.right = self.insertIntoBST(root.right,val)

        if root.val>val:
            root.left= self.insertIntoBST(root.left,val)

        return root