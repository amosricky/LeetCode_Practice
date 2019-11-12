# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: 'ListNode') -> 'ListNode':
        if (not head) or (not head.next):
            return head

        res = ListNode(head.val)
        resPoint = res
        point = head.next

        while point:
            if resPoint.val != point.val:
                resPoint.next = ListNode(point.val)
                resPoint = resPoint.next
                point = point.next
            else:
                point = point.next

        return res


node = ListNode(1)
node.next = ListNode(1)
node.next.next = ListNode(2)
node.next.next.next = ListNode(3)
node.next.next.next.next = ListNode(3)
# node.next.next.next.next.next = ListNode(5)

myClass = Solution()
result = myClass.deleteDuplicates(node)

while result:
    print(result.val)
    result = result.next
