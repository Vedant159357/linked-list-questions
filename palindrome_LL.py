# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head):
        prev,curr = None,head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr #moving to next node
            curr = nxt #curr moves to the temp node(before reversing next)
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True
        
        slow,fast = head,head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next

            fast = fast.next.next


        new_head = self.reverse(slow.next)

        #use two pointers to traverse and check
        first = head
        second = new_head

        while second is not None:
            if first.val != second.val:
                return False
            
            first = first.next
            second = second.next
        
        self.reverse(new_head)

        return True




        
