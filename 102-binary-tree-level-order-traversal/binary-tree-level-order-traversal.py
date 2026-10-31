# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        result=[]
        q=[]
        q.append(root)

        while q:
            s=len(q)
            level=[]

            for i in range(s):
                curr=q.pop(0)
                level.append(curr.val)
                if curr.left:
                    q.append(curr.left)

                if curr.right:
                    q.append(curr.right)
            result.append(level)
        return result