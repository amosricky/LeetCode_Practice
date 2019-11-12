# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: 'ListNode') -> 'ListNode':
        if not head:
            return head
        prePoint = ListNode(None)
        res = prePoint
        res.next = head

        while head and head.next:
            temp = head.next
            head.next = temp.next
            prePoint.next = temp
            temp.next = head
            prePoint = head
            head = head.next

        return res.next


root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)
myClass = Solution()
result = myClass.swapPairs(root)
while result:
    print(result.val)
    result = result.next
