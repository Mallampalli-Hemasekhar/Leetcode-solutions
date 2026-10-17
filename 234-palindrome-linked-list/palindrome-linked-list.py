# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        temp = head
        arr = []

        while temp is not None:
            arr.append(temp.val)
            temp = temp.next

        if arr == arr[::-1]:
            return True

        return False