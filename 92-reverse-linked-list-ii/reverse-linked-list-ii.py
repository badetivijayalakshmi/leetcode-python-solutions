# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        dummy = ListNode(0)
        dummy.next = head
        #Move prev to left-1 pos
        prev = dummy
        for _ in range(left-1):
            prev = prev.next
        curr = prev.next
        prev_rev = None
        #Reverse r-l+1 nodes
        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = prev_rev
            prev_rev = curr
            curr = nxt
        #Reconnect
        prev.next.next = curr
        prev.next = prev_rev
        return dummy.next

        