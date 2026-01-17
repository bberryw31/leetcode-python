# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return
        total_length = 0
        curr = head
        while curr:
            curr = curr.next
            total_length += 1
        target = total_length - n
        prev = None
        curr = head
        for i in range(target):
            prev = curr
            curr = curr.next
        if not prev:
            head = head.next
        else:
            prev.next = curr.next
        return head
        