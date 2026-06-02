# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        
        while len(lists) > 1:
            combinedLists = []
            for i in range(0, len(lists), 2):
                left = lists[i]
                right = lists[i+1] if (i+1) < len(lists) else None
                combinedLists.append(self.mergeLists(left, right))
            lists = combinedLists
        return lists[0]
    
    def mergeLists(self, left, right):
        head = ListNode(-1)
        tail = head

        while left and right:
            if right.val < left.val:
                tail.next = right
                right = right.next
            else:
                tail.next = left
                left = left.next

            tail = tail.next

        if left:
            tail.next = left
        if right:
            tail.next = right

        return head.next
            
            

        
        
        