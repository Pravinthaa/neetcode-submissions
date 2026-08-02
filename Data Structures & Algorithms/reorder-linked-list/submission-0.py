# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l1=head
        fast=head
        slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        a=slow.next
        slow.next=None
        curr=a
        prev=None
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        l2=prev
        while l2:
            nx=l1.next
            ny=l2.next
            l1.next=l2
            l2.next=nx
            l1=nx
            l2=ny
        
       

        

        