# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        pre = None
        cur = head
        nxt = head.next
        while cur and nxt:
            tmp = nxt.next
            nxt.next = cur
            cur.next = tmp
            if not pre:
                head = nxt
            else:
                pre.next = nxt
            pre = cur
            cur = pre.next
            if cur:
                nxt = cur.next
        return head


        