# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        m=0
        while curr:
            m+=1
            curr=curr.next
        e=m-n
        a=head
        if m==1 and n==1:
            return None
        if m==n:
            return head.next
        for i in range(1,e):
            a=a.next
        a.next=a.next.next
        return head

        