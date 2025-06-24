# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        start = head
        current = head
        previous = None
        count = 0
        while count < k:
            if not current:
                current = previous
                previous = None
                while current:
                    temp = current.next
                    current.next = previous
                    previous = current
                    current = temp
                return previous
            temp = current.next
            current.next = previous
            previous = current
            current = temp
            count += 1
        start.next = self.reverseKGroup(current, k)
        return previous