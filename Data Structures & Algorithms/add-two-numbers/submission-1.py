# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            tempsum = 0
            if l1:
                tempsum += l1.val
                l1 = l1.next
            if l2: 
                tempsum += l2.val
                l2 = l2.next
            tempsum += carry
            if tempsum >= 10:
                carry = 1
                tempsum %= 10
            else:
                carry = 0
            curr.next = ListNode(tempsum)
            curr = curr.next
        return dummy.next
