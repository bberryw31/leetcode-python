# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        current = head
        even = head.next
        is_even = False
        while current and current.next:
            temp = current.next
            if not current.next.next and is_even:
                current.next = current.next.next
                temp.next = even
                break
            elif not current.next.next and not is_even:
                current.next = even
                break
            else:
                current.next = current.next.next
            current = temp
            is_even = not is_even
        return head