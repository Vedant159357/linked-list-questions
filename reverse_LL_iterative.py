# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #iterative approach
        prev,curr = None,head

        while curr:
            nxt = curr.next #storing the next(pre-reverse) in a temp to not forget the next element after losing the point
            curr.next = prev
            prev = curr
            curr = nxt

        return prev
