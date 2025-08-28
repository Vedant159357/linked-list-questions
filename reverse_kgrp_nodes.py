# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLinkedList(self,head):
        temp = head
        prev = None

        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front

        return prev

    def getKthNode(self,temp,k):
        k -= 1

        while temp is not None and k > 0:
            k -= 1
            temp = temp.next
        
        return temp

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head

        prevLast = None

        while temp is not None:
            KthNode = self.getKthNode(temp,k)

            if KthNode is None:

                if prevLast:
                    prevLast.next = temp

                break
            
            nextNode = KthNode.next

            KthNode.next = None
            newHead = self.reverseLinkedList(temp)

            if temp == head:
                head = newHead
            
            else:
                prevLast.next = newHead

            prevLast = temp

            temp = nextNode
        
        return head
        
