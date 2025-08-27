# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        start = end = reverse_start = reverse_end = head
        for i in range(1, right + 1):
            if i + 1 < left:
                start = start.next
                reverse_start = reverse_start.next
            elif i + 1 == left:
                reverse_start = reverse_start.next
            if i < right:
                reverse_end = reverse_end.next
            end = end.next
        
        if left == 1:
            start = None
        
        print(start)
        print(end)
        print(reverse_start)
        print(reverse_end)

        reverse_end.next = None
        prev = None
        curr = reverse_start
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        if start:
            start.next = prev
        reverse_start.next = end
        return head if start else prev
        
