# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseNode(new_head):
            current = new_head
            previous = None
            while current:
                temp = current.next
                current.next = previous
                previous = current
                current = temp
            return previous
            
        def newHead(new_head, k):
            start = new_head
            current = new_head
            previous = None
            count = 0
            while count < k:
                if not current:
                    count = -1
                    break
                temp = current.next
                current.next = previous
                previous = current
                current = temp
                count += 1
            if count == -1:
                return reverseNode(previous)
            else:
                start.next = newHead(current, k)
            return previous

        if k == 1:
            return head
        return newHead(head, k)