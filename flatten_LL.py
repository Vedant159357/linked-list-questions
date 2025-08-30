'''
class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
        self.bottom = None
'''

class Solution:
    def merge(self, list1, list2):
        dummyNode = Node(-1)
        res = dummyNode

        while list1 and list2:
            if list1.data < list2.data:
                res.bottom = list1
                res = list1
                list1 = list1.bottom
            else:
                res.bottom = list2   # fixed: should be bottom not child
                res = list2
                list2 = list2.bottom
            res.next = None

        if list1:
            res.bottom = list1
        else:
            res.bottom = list2

        return dummyNode.bottom

    def flatten(self, root):
        if root is None or root.next is None:   # fixed: use root not head
            return root

        # recursively flatten the next list
        mergedHead = self.flatten(root.next)

        # merge current list with flattened next
        root = self.merge(root, mergedHead)

        return root
