# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0

        while curr is not None:
            length += 1
            curr = curr.next

        rem_len = length - n

        # Edge case: removing the head

        if rem_len == 0:
            return head.next

        curr = head

        while rem_len > 1:
            curr = curr.next
            rem_len -= 1

        # Remove the next node

        curr.next = curr.next.next

        return head