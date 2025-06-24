# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prev_end = None
        current = head
        while current:
            previous = None
            count = 0
            start = current
            while count < k:
                if not current:
                    current = previous
                    previous = None
                    while current:
                        temp = current.next
                        current.next = previous
                        previous = current
                        current = temp
                    prev_end.next = previous
                    return new_head
                temp = current.next
                current.next = previous
                previous = current
                current = temp
                count += 1
            if prev_end:
                prev_end.next = previous
            else:
                new_head = previous
            prev_end = start
        return new_head