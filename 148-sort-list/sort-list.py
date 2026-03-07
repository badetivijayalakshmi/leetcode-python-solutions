# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        #find middle
        slow = head
        fast = head.next #helps split evenly 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        right = slow.next
        slow.next = None
        #recursive calls
        left_sort = self.sortList(head)
        right_sort = self.sortList(right)
        #merge
        dummy = ListNode(0)
        curr = dummy
        while left_sort and right_sort:
            if left_sort.val < right_sort.val:
                curr.next = left_sort
                left_sort = left_sort.next
            else:
                curr.next = right_sort
                right_sort = right_sort.next
            curr = curr.next
        curr.next = left_sort if left_sort else right_sort
        return dummy.next
        