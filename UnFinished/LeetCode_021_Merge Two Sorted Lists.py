class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(None)
        resultPoint = result

        while l1 and l2:
            if(l1.val<l2.val):
                resultPoint.next = l1
                l1 = l1.next
            else:
                resultPoint.next = l2
                l2 = l2.next
            resultPoint = resultPoint.next
        resultPoint.next = l1 or l2

        return result.next
L1Node = ListNode(1)
L1Node.next = ListNode(2)
L1Node.next.next = ListNode(4)

L2Node = ListNode(1)
L2Node.next = ListNode(3)
L2Node.next.next = ListNode(4)

myClass = Solution()
result = myClass.mergeTwoLists(L1Node,L2Node)

while(result!=None):
    print(result.val)
    result = result.next