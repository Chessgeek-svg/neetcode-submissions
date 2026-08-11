# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lead = ListNode(None)
        lead.next = head
        lag = lead
        for i in range(n):
            lead = lead.next
        while lead.next:
            lead = lead.next
            lag = lag.next
        if lag.next == head:
            head = lag.next.next
        lag.next = lag.next.next
        return head
        