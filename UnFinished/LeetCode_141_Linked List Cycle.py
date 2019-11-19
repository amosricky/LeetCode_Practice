# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: 'ListNode') -> 'bool':
        res = False
        nodesList = []
        point = head

        while point != None:
            if not point in nodesList:
                nodesList.append(point)
                point = point.next
            else:
                res = True
                return res
        return res


root = ListNode(3)
root.next = ListNode(2)
root.next.next = ListNode(0)
root.next.next.next = ListNode(-1)
# root.next.next.next.next = root.next
myClass = Solution()
result = myClass.hasCycle(root)
print(result)