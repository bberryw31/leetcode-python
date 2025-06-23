# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        slow, fast = head, head
        slow_previous = slow
        while fast and fast.next:
            slow_previous = slow
            slow = slow.next
            fast = fast.next.next
        slow_previous.next = slow.next
        return head