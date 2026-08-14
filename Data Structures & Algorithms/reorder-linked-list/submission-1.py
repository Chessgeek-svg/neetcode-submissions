# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev, temp = None, slow.next
        slow.next = None
        while temp:
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt

        left, right = head, prev
        while left and right:
            left_next, right_next = left.next, right.next
            left.next = right
            left = left_next
            right.next = left
            right = right_next