# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Study order: 206 → 24 (this problem with k=2 hardcoded) → 92 → 25. If you can derive 25 from 206 rather than recalling it, you're prepared for the variants — reverse only the last partial group, reverse alternating groups, etc.

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth = self.get_kth(group_prev, k)
            if not kth:              # fewer than k nodes left → leave as-is
                break
            group_next = kth.next

            # reverse [group_prev.next ... kth], seeding prev with group_next
            prev, curr = group_next, group_prev.next
            while curr is not group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            tmp = group_prev.next    # old head = new tail of this group
            group_prev.next = kth    # old kth = new head of this group
            group_prev = tmp         # advance to the tail we just created

        return dummy.next


    def get_kth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr