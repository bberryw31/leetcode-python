# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        nums = [slow.val]
        max_sum = 0
        while fast.next.next:
            slow = slow.next
            fast = fast.next.next
            nums.append(slow.val)
        slow = slow.next
        while slow:
            max_sum = max(slow.val + nums.pop(), max_sum)
            slow = slow.next
        return max_sum