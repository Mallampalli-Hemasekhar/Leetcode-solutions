# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return
        a=[]
        curr=head 
        while curr is not None:
            a.append(curr)
            curr=curr.next
        
        i=0
        j=len(a)-1
        while i<j:
            a[i].next = a[j]
            i += 1
            if i == j:
                break
            a[j].next = a[i]
            j -= 1
        a[i].next = None
             
                





