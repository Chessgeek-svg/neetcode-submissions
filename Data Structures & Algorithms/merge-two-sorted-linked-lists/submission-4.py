# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        curr1, curr2, prev = list1, list2, None

        while curr1 and curr2:
            if curr1.val > curr2.val:
                temp = curr2
                curr2 = curr2.next
                temp.next = curr1
                if prev:
                    prev.next = temp
                prev = temp
            else:
                prev = curr1
                curr1 = curr1.next
        while curr2:
            if not prev:
                return list2
            prev.next = curr2
            prev = curr2
            curr2 = curr2.next
        if list2.val < list1.val:
            return list2
        return list1