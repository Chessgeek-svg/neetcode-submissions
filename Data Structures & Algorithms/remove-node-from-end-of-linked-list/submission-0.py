# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:
            curr = curr.next
            length += 1
        curr = head
        for i in range(length):
            if length - n == i:
                if i == 0:
                    head = head.next
                    break
                else:
                    prev.next = curr.next
                    break
            prev = curr
            curr = curr.next
        return head