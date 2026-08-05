class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head

        grpp = dummy

        while True:

            # find kth node
            a = grpp

            for i in range(k):
                a = a.next

                if not a:
                    return dummy.next

            # node after group
            grpn = a.next

            # disconnect group
            a.next = None

            # reverse group
            newh = self.reverse(grpp.next)

            # old head becomes tail
            temp = grpp.next

            # connect previous part
            grpp.next = newh

            # connect next group
            temp.next = grpn

            # move pointer
            grpp = temp


    def reverse(self, head):

        curr = head
        prev = None

        while curr:

            nextt = curr.next

            curr.next = prev

            prev = curr

            curr = nextt

        return prev