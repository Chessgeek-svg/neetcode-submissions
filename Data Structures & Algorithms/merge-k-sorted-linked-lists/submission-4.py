# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while len(lists) > 1:
            new_lists = []
            for i in range(0, len(lists), 2):
                left = lists[i]
                right = lists[i+1] if i+1 < len(lists) else []
                new_lists.append(self.mergeLists(left, right))
            lists = new_lists
        return lists[0] if lists else None
        

    def mergeLists(self, left, right):
        head = ListNode(-1)
        curr = head
        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
                curr = curr.next
            else:
                curr.next = right
                right = right.next
                curr = curr.next
        if left:
            curr.next = left
        if right:
            curr.next = right
        return head.next