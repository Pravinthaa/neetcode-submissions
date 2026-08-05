# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        curr=dummy
        car=0
        while l1 or l2 or car:
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0
            su= val1+val2+car
            car=su//10
            di=su%10
            curr.next=ListNode(di)
            curr=curr.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return dummy.next